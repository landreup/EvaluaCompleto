from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from evalua.views import listadoAlumnos, listadoProfesores, listadoCursos, nuevoCurso, nuevoProfesor, nuevoAlumno

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


""" URLs de Tutoritzacio """
urlpatterns = patterns('',
                       (r'^tutoritzacio/alumnes$', listadoAlumnos, {'rol': "tutor"}),
                       
    # Examples:
    # url(r'^$', 'prova.views.home', name='home'),
    # url(r'^prova/', include('prova.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

""" URLs de Coordinacio """
urlpatterns += (patterns('',
                        (r'^coordinacio/professorat$', listadoProfesores),
                        (r'^coordinacio/professorat/nou$', nuevoProfesor),
                        (r'^coordinacio/alumnes$', listadoAlumnos, {'rol': "coordinador"}),
                        (r'^coordinacio/alumnes/nou$', nuevoAlumno),
                        (r'^coordinacio/tutor/alumne$', listadoAlumnos, {'rol': 'coordinador-tutor'}),
                        (r'^coordinacio/cursos$', listadoCursos),
                        (r'^coordinacio/cursos/nou$', nuevoCurso),
                        
))


urlpatterns += staticfiles_urlpatterns()