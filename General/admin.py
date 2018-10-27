from django.contrib import admin

from .models import Documento, Alumno, Usuario, Profesor, Curso, Grupo, Logro, Logro_Estudiante, Evaluacion, Asignacion, Estudiante_Grupo, Asistencia, Evaluacion_Estudiante_Grupo

admin.site.register(Profesor)
admin.site.register(Usuario)
admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Grupo)
admin.site.register(Logro)
admin.site.register(Logro_Estudiante)
admin.site.register(Evaluacion)
admin.site.register(Asignacion)
admin.site.register(Estudiante_Grupo)
admin.site.register(Asistencia)
admin.site.register(Evaluacion_Estudiante_Grupo)
admin.site.register(Documento)

