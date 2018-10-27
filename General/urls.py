from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ayuda', views.ayuda, name='help'),
    path('ayuda/file', views.ayudafile, name='helpfile'),
    path('acercade', views.acercade, name='acercade'),
]