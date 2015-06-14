from django.conf.urls import patterns,include,url

urlpatterns = patterns('apprest.api.views',
	url(r'^hijos/$','hijos',name = 'hijos'),
	url(r'^hijos/(?P<id>\d+)/$','hijos' , name = 'hijos'),
	url(r'^padres/$','padres', name = 'padres'),
	url(r'^padres/(?P<id>\d+)/$','padres',name = 'padres'),
	)