from django.shortcuts import render
from django.http import HttpResponseRedirect
from General.models import *
from General.forms import *
import datetime 

def main(request):
	if request.method == 'POST':
		return HttpResponseRedirect('/general/main')
	else:
		grados = ["Primer grado", "Segundo grado", "Tercer grado", "Cuarto grado", "Quinto grado", "Sexto Grado"]
		identifier = request.session['ID']
		profesor = Profesor.objects.get(id = identifier)
		grupos = Grupo.objects.filter(profesor = profesor).order_by('grado')
		materias = []
		asignaciones = []
		fecha= datetime.datetime.now()
		for i in grupos:
			if(i.anno == str(fecha.year)):
				materias.append(i)
				evaluaciones = Evaluacion.objects.filter(grupo = i)
				for j in evaluaciones:
					asig = Asignacion.objects.filter(evaluacion = j)
					for k in asig:
						if((fecha.date() -k.fecha).days <= 7):
							asignaciones.append(k)


	return render(request, 'Profesor/MainProfesor.html', {"grados": grados ,"materias": materias, "asignaciones": asignaciones})	


def curso(request, identifier):
	grupo = Grupo.objects.get(id = identifier)
	request.session['grupo']= identifier
	evaluaciones = Evaluacion.objects.filter(grupo = grupo)
	asignaciones = Asignacion.objects.filter(evaluacion__in = evaluaciones)
	return render(request, 'Profesor/CursoProfesor.html', {"grupo": grupo, "evaluaciones":evaluaciones, "asignaciones":asignaciones})

def crearLogro(request):
	if request.method == 'POST':
		form = LogroForm(request.POST)
		if form.is_valid():
			titulo = form.cleaned_data['titulo']
			detalle = form.cleaned_data['detalle']
			grupo= Grupo.objects.get(id = request.session['grupo'])
			logro = Logro(nombre= titulo , descripcion= detalle , grupo= grupo )
			logro.save()
			return HttpResponseRedirect('/profesor/curso/'+str(request.session['grupo']))
	else:
		form = LogroForm()
	return render(request, 'Profesor/CrearLogroProfesor.html', {'form': form})	

def logro(request):
	grupo = Grupo.objects.get(id = request.session['grupo'])
	logros = Logro.objects.filter(grupo = grupo)
	return render(request, 'Profesor/LogroProfesor.html', {'logros': logros})

def crearAsignacion(request,identifier):
	if request.method == 'POST':
		print(request.POST)
		print(request.FILES)
		nombre = request.POST.get("nombre", "")
		detalle = request.POST.get("detalle", "")
		valor = request.POST.get("valor", "")
		fecha = request.POST.get("fecha", "")
		asignacion = Asignacion.objects.get(id = identifier)
		asignacion.nombre = nombre
		asignacion.detalle = detalle
		asignacion.valor = valor
		asignacion.fechaFinal = fecha
		#asignacion = Asignacion(nombre= titulo , detalle= detalle, valor_porcentual = valor, fechaFinal = datetime.datetime.now().date() )
		asignacion.save()

		is_private = request.FILES.get('file', False)
		if is_private:
			doc1 = Documento.objects.filter(asignacion = asignacion)
			if(len(doc1)>0):
				i = doc1[0]
				i.delete()
			
			newdoc = Documento(filename = "12345" ,docfile = request.FILES['file'], asignacion= asignacion)
			newdoc.save()
		return HttpResponseRedirect('/profesor/curso/'+str(request.session['grupo']))

	else:
		asignacion = Asignacion.objects.get(id = identifier)
		doc1 = Documento.objects.filter(asignacion = asignacion)
		if(len(doc1)>0):
			doc= "Archivo actual: "+str(doc1[0].docfile)
		else:
			doc= "Archivo actual: No se ha cargado ningún archivo"

	return render(request, 'Profesor/crearAsignacionProfesor.html', {'doc':doc , 'asignacion': asignacion})

def table(request):
	if request.method == 'POST':
		print(str(request.POST))
		return HttpResponseRedirect('/')
	else:
		usuarios = Usuario.objects.all()
		
	return render(request, 'Profesor/table.html', {"usuarios": usuarios})

def perfil(request):
	profesor = Profesor.objects.get(id = request.session['ID'])
	grupo = Grupo.objects.filter(profesor= profesor)
	evaluaciones = Evaluacion.objects.filter(grupo__in = grupo)
	asignaciones = Asignacion.objects.filter(evaluacion__in = evaluaciones, isrevisado = 0)
	return render(request, 'Profesor/PerfilProfesor.html', {"profesor": profesor, "asignaciones": asignaciones})	

def agregarAsistencia(request):
	if request.method == 'POST':
		grupo = Grupo.objects.get(id = request.session['grupo'])
		alumnos = Estudiante_Grupo.objects.filter(grupo = grupo)
		cont= 1
		val= request.POST.get("fc"+str(cont)+"1", "")
		valores=[]
		while(val != ""):
			lista = []
			cont2 = 1
			val2= request.POST.get("ck"+str(cont2)+str(cont)+"1", "")
			while(val2 != ""):
				if(val2 == "Si"):
					lista.append(1)
				else:
					lista.append(0)
				cont2+=1
				val2= request.POST.get("ck"+str(cont2)+str(cont)+"1", "")
			cont+=1
			valores.append((val,lista))
			val= request.POST.get("fc"+str(cont)+"1", "")
		guardarAsistencia(list(alumnos),valores)
		return HttpResponseRedirect('/profesor/curso/'+str(request.session['grupo']))
	else:
		grupo = Grupo.objects.get(id = request.session['grupo'])
		alumnos1 = Estudiante_Grupo.objects.filter(grupo = grupo)
		oneday=datetime.timedelta(days=15)
		day= datetime.datetime.now().date()-oneday
		asistencia = Asistencia.objects.filter(alumno__in = alumnos1 , fecha__gte=  day ).order_by('fecha')
		fechas=[]
		alumnos=[]
		for i in asistencia:
			if i.fecha not in fechas:
				fechas.append(i.fecha)
		for i in alumnos1:
			lista=[]
			for j in asistencia:
				if i == j.alumno:
					lista.append(j.asistio)
			alumnos.append((i,lista))
	return render(request, 'Profesor/CalificarAsistenciaProfesor.html', {"alumnos": alumnos, "fechas":fechas, "asistencias":asistencia})

def asistencia(request):
	grupo = Grupo.objects.get(id = request.session['grupo'])
	alumno = Estudiante_Grupo.objects.filter(grupo = grupo)
	alumnos=[]
	for i in alumno:
		asistencia = Asistencia.objects.filter(alumno = i, asistio= 0)
		alumnos.append((i,len(asistencia)))
	return render(request, 'Profesor/AsistenciaProfesor.html', {"alumnos": alumnos})

def logout(request):
	request.session['ID']= 0
	return HttpResponseRedirect('/')


def asignacion(request, identifier):
	asignacion = Asignacion.objects.get(id = identifier)
	documento = Documento.objects.filter(asignacion = asignacion)
	exist=0
	if(len(documento)>0):
		exist=1
	return render(request, 'Profesor/AsignacionProfesor.html', {"asignacion":asignacion, "exist":exist})

def otorgarLogro(request, identifier):
	if request.method == 'POST':
		cont=1
		valores=[]
		val= request.POST.get("btnAddCol"+str(cont)+"1", "")
		while(val != ""):
			num = request.POST.get("btnAddCol"+str(cont)+"2", "")
			valores.append((val,num))
			cont+=1
			val= request.POST.get("btnAddCol"+str(cont)+"1", "")
		for i in valores:
			estado = Logro_Estudiante.objects.filter(alumno= i[1], logro= request.session['LOGRO']).exists()
			if estado and i[0]=="No": 
				Logro_Estudiante.objects.filter(alumno= i[1], logro= request.session['LOGRO']).delete()
			elif estado==False and i[0]=="Si":
				logro = Logro_Estudiante(alumno= Alumno.objects.get(id= i[1]), logro= Logro.objects.get(id= request.session['LOGRO']))
				logro.save()
				
		return HttpResponseRedirect('/profesor/logro')
	else:
		request.session['LOGRO']= identifier
		logro= Logro.objects.get(id = identifier)
		alumnos1 = Estudiante_Grupo.objects.filter(grupo = logro.grupo)
		alumnos = []
		for i in alumnos1:
			alumnos.append(i.alumno)
		alumnos_logro = Logro_Estudiante.objects.filter(logro = logro, alumno__in = alumnos).values_list('alumno', flat=True)
	return render(request, 'Profesor/OtorgarLogrosProfesor.html', {"logro":logro, "alumnos": alumnos, "alumnos_logro": alumnos_logro})


def guardarAsistencia(alumnos, valores):
	for fecha,valor in valores:
		for i in range(0,len(valor)):
			if Asistencia.objects.filter(alumno=alumnos[i], fecha=fecha).exists():
				asistencia = Asistencia.objects.filter(alumno=alumnos[i], fecha=fecha)
				asistencia = asistencia[0]
				if( asistencia.asistio != valor[i] ):
					asistencia.asistio= valor[i]
					asistencia.save()
			else:
				asistencia = Asistencia(alumno= alumnos[i], asistio= valor[i] , fecha= fecha)
				asistencia.save()


def crearEvaluacion(request):
	if request.method == 'POST':
		print(request.POST)
		asignacionesViejas= []
		asignacionesNuevas= []
		grupo = Grupo.objects.get(id = request.session['grupo'])
		evaluaciones = Evaluacion.objects.filter(grupo= grupo)
		for i in  evaluaciones:
			asignaciones = Asignacion.objects.filter(evaluacion = i)
			for i in asignaciones:
				valor = i
				val = request.POST.get("ID"+str(i.id), "")
				num = float(request.POST.get("VAL"+str(i.id), ""))
				est = False
				if(valor.nombre != val):
					valor.nombre = val
					est = True
				if(valor.valor_porcentual != num):
					valor.valor_porcentual = num
					est = True
				if(est):
					valor.save()
		cont = 1
		val = request.POST.get("newName1", "")
		lista = (request.POST.get("lista", ""))
		lista = (lista[1:len(lista)-1]).split(",")
		while(val != ""):
			nombre= request.POST.get("newName"+str(cont), "")
			porcentaje= float(request.POST.get("newVal"+str(cont), ""))
			evaluacion = Evaluacion.objects.get(id = lista[int(request.POST.get("newEva"+str(cont), ""))-1])
			asignacion = Asignacion(nombre= nombre, detalle="", valor_porcentual= porcentaje, evaluacion= evaluacion, fecha = datetime.datetime.now().date(), fechaFinal = datetime.datetime.now().date(), isrevisado=0)
			asignacion.save()
			cont+= 1
			val = request.POST.get("newName"+str(cont), "")


		#print(asignacionesNuevas)
		return HttpResponseRedirect('/profesor/curso/'+str(request.session['grupo']))
	else:
		print("Adios")
		grupo = Grupo.objects.get(id = request.session['grupo'])
		evaluaciones1 = Evaluacion.objects.filter(grupo= grupo)
		valores = list(Evaluacion.objects.filter(grupo= grupo).values_list('id', flat=True))
		evaluaciones= []
		for i in  evaluaciones1:
			asignaciones = Asignacion.objects.filter(evaluacion = i)
			evaluaciones.append((i,asignaciones))
	return render(request, 'Profesor/EvaluacionesProfesor.html', {"evaluaciones":evaluaciones, "valores": valores})







