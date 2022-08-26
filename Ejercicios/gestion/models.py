from django.db import models
from autorizacion.models import Usuario

# Create your models here.
#from autorizacion.models import Usuario

class Tarea(models.Model):
    # TIPOS DE DATOS > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-types
    # OPCIONES DE LAS COLUMNAS > https://docs.djangoproject.com/en/4.0/ref/models/fields/#field-options
    estadoOpciones = [('POR_HACER', 'POR_HACER'), ('HACIENDO', 'HACIENDO'), ('HECHO', 'HECHO')]

    id = models.AutoField(primary_key=True, unique=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True)
    fechaVencimiento = models.DateTimeField(db_column='fecha_vecimiento')
    estado = models.CharField(choices=estadoOpciones, max_length=10, default='POR_HACER')
    
    '''
    			Relacion entre el Modelo Tarea y Usuario
    			
    >>> on_delete : sirve para indicar que accion se debe de realizar sobre los registros que pertenecen a ese registro a eliminar y sus valores pueden ser:
    
	    # CASCADE : Elimina el usuario y  elimina a sus tareas.
	    # PROTECT : Evita la eliminacion del usuario lanzando un error.
	    # SET_NULL : Elimina el usuario y a todas sus tareas les cambia el valor de usuario_id a NULL.
	    # SET_DEFAULT(valor) : Elimina el usuario y modifica su valor a un valor por defecto.
    
    # related_name : Sirve para que a raiz del modelo usuario este cree un atributo en la clase Usuario para poder acceder a todas sus tareas si no se define el valor predeterminado sera
    '''
    usuario_set_tarea
    usuarioId = models.ForeignKey(to=Usuario, related_name='tareas', db_column='usuario_id', on_delete=models.CASCADE)

    class Meta:
        # https://docs.djangoproject.com/en/4.0/ref/models/options/
        db_table = 'tareas'
        # el ordenamiento sera de manera descendente por la columna fecha_vencimiento
        ordering = ['-fechaVencimiento'] 
