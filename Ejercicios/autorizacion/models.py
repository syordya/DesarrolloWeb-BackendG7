from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

"""Clase que sirve para manejar el comportamiento al crear el usuario con el comando """
class ManejoUsuario(BaseUserManager):
    def create_user(self, correo, nombre, apellido, password):
        if not correo:
            raise ValueError('El Correo es Obligatorio')
            
        # Eliminacion de caracteres especiales
        # Eliminacion de los Espacios en Blanco
        correo = self.normalize_email(correo)
        
        # Crear Nuevo Usuario
        nuevo_Usuario = self.model(correo=correo, nombre=nombre, apellido=apellido)
        
        # Cifrado del Paswword
        # Tecnica : Hash
        # Generar un string aleatorio tomando como base la contraseña original
        nuevo_Usuario.set_password(password)

        nuevo_Usuario.save()
        return nuevo_Usuario
        
        
        '''
        En este metodo se crea un SuperUsuario.
        Se solicita su funcion cuando es llamado por consola
        '''
    def create_superuser(self, correo, nombre, apellido, password):
        nuevo_Usuario = self.create_user(correo, nombre, apellido, password)
        
        # Modificar los valores que son correspondientes a un super usuario
        nuevo_Usuario.is_superuser = True
        nuevo_Usuario.is_staff = True
        nuevo_Usuario.save()


class Usuario(AbstractBaseUser):
    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    correo = models.EmailField(unique=True)
    password = models.TextField()
    
    #  Se ejecuta si aun vamos a utilizar el panel administrativo (CMS (Control Management Sytem)) 

    # es_Staff  : Indica si el usuario pertenece al staff que puede ingresar al CMS
    es_Staff = models.BooleanField(default=False)
    
    # esta_Activo : Indica si el usuario esta activo y por lo tanto puede tener acceso al CMS, 
    #             si no esta activo aun asi sea staff no podra ingresar
    esta_Activo = models.BooleanField(default=True)
    
    # python manage.py createsuperuser
    objects = ManejoUsuario()

    # Solicita el Nombre_Usuario al momento de Logearse 
    USERNAME_FIELD = 'correo'

    REQUIRED_FIELDS = ['nombre', 'apellido']

    class Meta:
        db_table = 'usuarios'
