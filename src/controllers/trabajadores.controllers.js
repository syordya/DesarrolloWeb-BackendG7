import { trabajadoresRequestDTO, cambiarPasswordRequestDTO, loginRequestDTO } from '../dtos/trabajadores.dto.js';
import bcryptjs from "bcryptjs";
import cryptoJs from "crypto-js";
import {PrismaConnector} from "../prisma.js"
import { validarCorreo, cambioPassword } from '../utils/correos.js';
import jwt from 'jsonwebtoken';

// porque hay librerias que han sido desarrolladas en CommonJS y como el proyecto esta siendo realizado en EsModule entonces no se logran entender por lo que hay que importar la libreria en su totalidad y luego recien hacer la destructuracion
const { compareSync }=bcryptjs;

export const postTrabajador=async(req,res)=>{
    try {
        const {password, ...data}=trabajadoresRequestDTO(req.body);
        const password_encriptada= bcryptjs.hashSync(password,10);
        console.log(password_encriptada);

        const result= await PrismaConnector.trabajador.create({data:{ ...data,password:password_encriptada},
        });


        const horaActual= new Date()
        const token=cryptoJs.AES.encrypt(JSON.stringify({
            id: result.id,
            caducidad: new Date(
                horaActual.getFullYear(),
                horaActual.getMonth(),
                horaActual.getDate(),
                horaActual.getHours() + 2
              ),
            }),
              process.env.LLAVE_ENCRIPTACION
         ).toString();


        await validarCorreo({
            destinatario:result.email,
            nombre:result.nombre, 
            token
        });

        return res.json({
            message:"Usuario registrado exitosamente",
            result,
        });
    } catch (error) {
        return res.status(400).json({
            message:"Error al crear el usuario",
            result: error.message,
        });
    }
};

export const validarTrabajador=async(req,res)=>{
    const {token}=req.body;
    try {
    
       const data= cryptoJs.AES.decrypt(token,process.env.LLAVE_ENCRIPTACION).toString(cryptoJs.enc.Utf8);
       console.log(data);

    //    la desencriptacion si es que la token es invalida retornara null entonces forzamos el errror con el siguiente IF

        if (!data) {
            throw new Error('Token no valida')
        }


        const infoToken=JSON.parse(data);
        console.log(infoToken);
        if(infoToken.caducidad< new Date()){
            throw new Error('La token ya venció');
        }

        // busco al trabajador
        const trabajador= await PrismaConnector.trabajador.findUniqueOrThrow({
            where:{id:infoToken.id},
        })
        // verifico que no esté validado
        if (trabajador.validado) {
            throw new Error("Usuario ya fue validado");
        }
        // valido
        await PrismaConnector.trabajador.update({
            data:{validado:true},
            where:{id:infoToken.id}
        });


       return res.json({
        message:"Trabajador validado exitosamente",
        result:null,
       })

        
    } catch (error) {
        return res.status(400).json({
            message:"Error al validar la token",
            result: error.message
        });
    }
    
};

export const cambiarPassword = async (req, res) => {
    try {
      const data = cambiarPasswordRequestDTO(req.body);
  
      const trabajador = await PrismaConnector.trabajador.findUniqueOrThrow({
        where: { email: data.email },
      });
      // TODO: que las contraseñas no pueden ser iguales la nueva que la anterior
  
      if (bcryptjs.compareSync(data.antiguaPassword, trabajador.password)) {
        const nuevaPassword = bcryptjs.hashSync(data.nuevaPassword);
  
        await PrismaConnector.trabajador.update({
          data: {
            password: nuevaPassword,
          },
          where: {
            email: data.email,
          },
        });
  
        await cambioPassword({
          destinatario: trabajador.email,
          nombre: trabajador.nombre,
        });
        return res.json({
          message: "Contraseña actualizada exitosamente",
          result: null,
        });
      } else {
        throw new Error("La contraseña es incorrecta");
      }
    } catch (error) {
      return res.json({
        message: "Error al actualizar la password",
        result: error.message,
      });
    }
  };

export const login=async(req,res)=>{
    const{body}=req;
    try {
      const data=loginRequestDTO(body);
      const trabajador= await PrismaConnector.trabajador.findUniqueOrThrow({
        where:{email:data.email},
      });

      if(compareSync(data.password,trabajador.password)){
        console.log('si es la password');
        const token=jwt.sign({
          id: trabajador.id,
          message:'Mensaje oculto',
        },process.env.JWT_SECRET,
        {expiresIn:'2h'}
        // expiresIn: un numero sera segundos, si es un numero con comillas sera ms, '1 day','10h','50d','1y'
        );
        return res.json({
          message:"Bienvenido",
          result:token,
        });
      }else{
        console.log('contraseña incorrecta');

        throw new Error("Password invalida");
      }
    } catch (error) {
      return res.status(400).json({
        message: "Error al hacer el login",
        result: error.message,
      })
    }
}

export const perfil = async(req,res)=>{
  console.log(req.user);
  const {password, ...result}=req.user;
  return res.json({
    message:null,
    result,
  });
};