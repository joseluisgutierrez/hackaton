from django.db import models
from django.utils.encoding import smart_unicode
# Create your models here.

class Hijo(models.Model):
	
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique = True)
    genero = models.CharField(max_length = 5)
    direccion = models.CharField(max_length = 200)
    fechaNaci = models.DateField('Fecha de nacimiento')
    

    def __unicode__(self):
    	return smart_unicode(self.nombre + " " + self.apellido) 


class Padre(models.Model):

	nombres = models.CharField(max_length = 100)
	apellidos = models.CharField(max_length = 100)
	dni = models.CharField(max_length = 8, unique = True)
	Shijos = models.ForeignKey(Hijo,related_name = 'Shijos')
	def __unicode__(self):
		return smart_unicode(self.nombres + " " + self.apellidos)