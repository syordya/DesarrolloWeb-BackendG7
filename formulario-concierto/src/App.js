import { useState  } from 'react';
import fondo from "./img/fondo.jpg"
import './App.css';
import {crearParticipantes} from "./services/participantes.services"

function App() {
  const [input, setInput] = useState({
    nombre:'',
    apellido:'',
    correo:'',
    password:'', 
    comentario:'',
    zona:'G' 
  });
  const [checkbox, setCheckbox]=useState(false)
  const handleChange = ({target}) => {
    setInput({
      ...input,
      [target.name]:target.value
    })
  }
  const cambio = ()=>{
    setCheckbox(!checkbox)
  }

  const envio=async (e)=>{
    e.preventDefault()
    const guardar= await crearParticipantes(input)
    console.log(guardar)
  }
  return (
   <div className="container">
      
    <img src={fondo} alt="musica"/>
           
      <form className="registro" onSubmit={envio}>
          <h3>Registro</h3>
          <input className="datos"
            type="text" 
            placeholder="Nombre"
            name="nombre"
            value={input.nombre}
            onChange={handleChange}></input>
          <input className='datos'
            type="text" 
            placeholder="Apellido"
            name='apellido'
            value={input.apellido}
            onChange={handleChange}></input>
          <input className="datos" 
            type="email" 
            placeholder="Correo"
            name="correo"
            value={input.correo}
            onChange={handleChange}></input>
          <input className='datos'
            type="password" 
            placeholder="password"
            name='password'
            value={input.password}
            onChange={handleChange}></input>
          <h4>Zonas</h4>
          <label> Selecciona la zona de tu preferencia</label>
          
          <div className="selec">
            <input type="radio" value="SUPER_VIP" name="zona" id="sp"  onChange={handleChange}/>
            <label htmlFor="sp">Super Vip</label>
          </div> 
          <div className="selec"> 
            <input type="radio" value="VIP" name="zona" id="v"  onChange={handleChange}/>
            <label htmlFor="v"> Vip</label>
          </div> 
          <div className="selec"> 
            <input type="radio" value="GENERAL" name="zona" id="g"  onChange={handleChange}/>
            <label htmlFor="g"> General</label>
          </div>   
          <textarea
            rows="5"
            name="comentario"
            value={input.comentario}
            onChange={handleChange}/>
          <div>
            <input type="checkbox" value="TC" name="acepto" id="check"  checked={checkbox} onChange={cambio}></input>
            <label htmlFor="check">Acepto los terminos y condiciones</label>
          </div> 
          <div className="boton">
            <button type='submit'>Registrarme</button>
          </div>     
          
      </form>
    </div>
  );
}

export default App;
