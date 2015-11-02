from django.contrib import admin

from .models import *

#-------------------------------------------------------------------------

@admin.register(Persona)
class PersonaAdmin(admin.ModelAdmin):
	list_display = ['__unicode__', 'direccion', 'telefono']
	ordering = ['nombre']