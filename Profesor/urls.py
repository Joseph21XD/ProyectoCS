from django.urls import include, path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('curso/<int:identifier>', views.curso, name='curso'),
    path('logro/add', views.crearLogro, name='crearLogro'),
    path('logro', views.logro, name='logro'),
    path('logro/<int:identifier>', views.otorgarLogro, name='otorgarLogro'),
    path('asignacion/<int:identifier>/edit', views.crearAsignacion, name='crearAsignacion'),
    path('evaluacion/add', views.crearEvaluacion, name='crearEvaluacion'),
    path('asignacion/<int:identifier>', views.asignacion, name='asignacion'),
    path('table', views.table, name='table'),
    path('perfil', views.perfil, name='perfil'),
    path('asistencia', views.asistencia, name='asistencia'),
    path('asistencia/add', views.agregarAsistencia, name='agregarAsistencia'),
    path('logout', views.logout, name='logout'),
]