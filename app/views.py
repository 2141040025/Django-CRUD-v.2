from django.shortcuts import render, get_object_or_404, redirect

from .models import Persona
from .forms import PersonaForm
#-------------------------------------------------------------------------

def pagina_inicio(request):
	personas = Persona.objects.all()

	context = {
		'personas': personas
	}

	return render(request, 'pagina_inicio.html', context)

#-------------------------------------------------------------------------

def ver_persona(request, id):
	persona = get_object_or_404(Persona, id=id)

	context = {
		'persona' : persona,
	}

	return render(request, 'ver_persona.html', context)
	
#-------------------------------------------------------------------------

def editar_persona(request, id):
	persona = get_object_or_404(Persona, id=id)
	form = PersonaForm(request.POST or None, request.FILES or None, instance=persona)


	if form.is_valid():
		form.save()
		return redirect('/')


	context = {
		'persona': persona,
		'form': form,
	}


	return render(request, 'editar_persona.html', context)

#-------------------------------------------------------------------------

def crear_persona(request):
	form = PersonaForm(request.POST or None, request.FILES or None)


	if form.is_valid():
		form.save()
		return redirect('/')


	context = {
		'form': form,
	}


	return render(request, 'editar_persona.html', context)

#-------------------------------------------------------------------------

def borrar_persona(request, id,):

	persona = get_object_or_404(Persona, id=id)

	if request.method == 'POST':
		persona.delete()
		return redirect('/')

	context = {
		"persona": persona,
	}

	return render(request, "confirmar_borrar.html", context)	