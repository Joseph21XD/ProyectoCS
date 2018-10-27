from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from General.models import *
from General.forms import *
import datetime 

def main(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/general/main')
	else:
		identifier = request.session['ID']
		alumno = Alumno.objects.get(id = identifier)
		materiasTotal = Estudiante_Grupo.objects.filter(alumno = alumno)
		materias = []
		asignaciones = []
		fecha= datetime.datetime.now()
		for i in materiasTotal:
			if(i.grupo.anno == str(fecha.year)):
				materias.append(i.grupo)
				evaluaciones = Evaluacion.objects.filter(grupo = i.grupo)
				for j in evaluaciones:
					asig = Asignacion.objects.filter(evaluacion = j)
					for k in asig:
						if((fecha.date() -k.fecha).days <= 7):
							asignaciones.append(k)
	return render(request, 'Alumno/MainEstudiante.html', {"materias": materias, "asignaciones": asignaciones})

def curso(request, identifier):
	grupo = Grupo.objects.get(id = identifier)
	alumno = Alumno.objects.get(id = request.session['ID'])
	evaluaciones = Evaluacion.objects.filter(grupo = grupo)
	asignaciones = Asignacion.objects.filter(evaluacion__in = evaluaciones)
	logros_persona = Logro_Estudiante.objects.filter(alumno = alumno)
	ids=[]
	for i in logros_persona:
		ids.append(i.logro.id)
	logros = Logro.objects.filter(grupo = grupo).exclude(id__in = ids)

	return render(request, 'Alumno/CursoEstudiante.html', {"curso": grupo, "evaluaciones":evaluaciones, "asignaciones":asignaciones, "logros": logros})


def asignacion(request, identifier):
	asignacion = Asignacion.objects.get(id = identifier)
	documento = Documento.objects.filter(asignacion = asignacion)
	exist=0
	if(len(documento)>0):
		exist=1
	return render(request, 'Alumno/AsignacionEstudiante.html', {"asignacion":asignacion, "exist":exist})

def asignacionDownload(request, identifier):
	asignacion = Asignacion.objects.get(id = identifier)
	file= Documento.objects.filter(asignacion = asignacion)
	filename = file[0].docfile.name.split('/')[-1]
	response = HttpResponse(file[0].docfile, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response

def perfil(request):
	alumno = Alumno.objects.get(id = request.session['ID'])
	alumno_grupo = Estudiante_Grupo.objects.filter(alumno = alumno)
	logros = Logro_Estudiante.objects.filter(alumno = alumno)
	fecha= datetime.datetime.now()
	grupo = []
	for i in alumno_grupo:
		if(i.grupo.anno == str(fecha.year)):
			grupo.append(i.grupo)
	return render(request, 'Alumno/PerfilEstudiante.html', {"alumno":alumno,"logros":logros, "grupo": grupo[0]})

def logout(request):
	request.session['ID']= 0
	return HttpResponseRedirect('/')


