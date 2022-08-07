'''
>>> Crear una Clase Persona en la cual se guarden : 

    - Nombre
    - Fecha_Nacimiento
    - Nacionalidad 
    - DNI 

>>> Tambien una clase Alumno y una clase Docente 
    en la cual el Alumno a difrencia del docente
    tenga una serie de cursos matriculados, y
    el Docente por su parte tenga :

    - Numero_Seguro_Social
    - Cuenta_CTS 

>>> En base a lo visto de herencia crear las clases y 
    ademas ver si hay algun atributo o metodo que 
    deba de ser privado.

'''

class Persona:
    def __init__(self,nombre,fecha_nac,nacionalidad,dni):
        self.nombre = nombre
        self.fecha_nac = fecha_nac
        self.nacionalidad = nacionalidad
        self.dni = dni
    
    def info(self):
        return{
            'nombre' : self.nombre,
            'fecha_nac' : self.fecha_nac,
            'nacionalidad' : self.nacionalidad,
            'DNI' : self.dni
        }

class Profesor(Persona):
    def __init__(self,nombre,fecha_nac,nacionalidad,dni,cts,seg_social):
        self.cts = cts
        self.seguro_social = seg_social
        super().__init__(nombre,fecha_nac,nacionalidad,dni)

    def info(self):
        info_prosor = super().info()
        datos = {
            'cts': self.cts,
            'seguro_social' : self.seguro_social
            }
        return {**info_prosor, **datos}

class Alumno(Persona):
    def __init__(self,nombre,fecha_nac,nacionalidad,dni,*cursos):
        self.cursos = cursos
        super().__init__(nombre,fecha_nac,nacionalidad,dni)

    def info(self):
        info_alumno = super().info()
        datos = {
            'cursos' : self.cursos
        }
        return {**info_alumno, **datos }


if __name__=="__main__":

    print(" *********** DATOS --- ALUMNO *********** ")
    alumno1 = Alumno('Yordy Williams Santos Apaza',"24/12/96","Peruano","12345678","Big Data","Tesis 2","Deep Learning")
    #print("Alumno1, cursos matriculados: {}".format(alumno1.cursos))
    print(alumno1.info())

    print(" *********** DATOS --- PROFESOR *********** ")
    prosor1 = Profesor("Alvaro Henry Mamani Aliaga", "06/06/66","Boliviano","333666999","2000","12345")
    #print("Docente1 su cuenta de CTS es: {}".format(prosor1.cts))
    print(prosor1.info())




