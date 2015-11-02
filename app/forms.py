# -*- coding: utf-8 -*-
from django import forms

from .models import Persona

#-------------------------------------------------------------------------

class PersonaForm(forms.ModelForm):
	
	apellido_paterno = forms.CharField(label='Apellido Paterno')
	apellido_materno = forms.CharField(label='Apellido Materno')

	class Meta:
		model = Persona
		fields = ['nombre', 'apellido_paterno', 'apellido_materno', 'direccion', 'telefono', 'foto',]