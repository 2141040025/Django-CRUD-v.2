from django.db import models

#-------------------------------------------------------------------------

class Persona(models.Model):

	nombre = models.CharField(max_length=200)
	apellido_paterno = models.CharField(max_length=200)
	apellido_materno = models.CharField(max_length=200)
	direccion = models.CharField(max_length=250)
	telefono = models.CharField(max_length=250, blank=True)
	foto = models.ImageField(upload_to='persona')

	class Meta:
		verbose_name = "Persona"
		verbose_name_plural = "Personas"
		ordering = ['apellido_paterno']

	def __unicode__(self):
		return "%s %s" % (self.nombre, self.apellido_paterno)

#-------------------------------------------------------------------------
    