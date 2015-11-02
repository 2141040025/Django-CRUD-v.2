from django.conf.urls.static import static
from django.conf.urls import include, url
from django.contrib import admin

from . import views
from CRUD_1 import settings
#-------------------------------------------------------------------------

urlpatterns = [


	# Pagina_Principal
	url(r'^$', views.pagina_inicio),

	# Ver
	url(r'^persona/(?P<id>\d+)$', views.ver_persona, name='ver'),

	# Editar
	url(r'^persona/editar/(?P<id>\d+)$', views.editar_persona, name="editar"),

	# Crear
	url(r'^persona/crear/$', views.crear_persona, name='crear'),

	# Borrar
	url(r'^persona/borrar/(?P<id>\d+)$', views.borrar_persona, name='borrar'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
