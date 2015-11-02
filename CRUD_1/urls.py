
from django.conf.urls import include, url
from django.contrib import admin

#-------------------------------------------------------------------------

urlpatterns = [



	# Main App
	url(r'', include('app.urls')),


	# Admin
    url(r'^admin/', include(admin.site.urls)),





]
