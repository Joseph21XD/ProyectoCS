from django.urls import include, path
from . import views

urlpatterns = [
    path('main', views.main, name='main'),
    path('curso/<int:identifier>', views.curso, name='curso'),
    path('asignacion/<int:identifier>', views.asignacion, name='asignacion'),
    path('asignacion/<int:identifier>/file', views.asignacionDownload, name='asignacionDownload'),
    path('perfil', views.perfil, name='perfil'),
    path('logout', views.logout, name='logout'),
]