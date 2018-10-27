from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse

from .models import *
from .forms import *

def index(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			user = form.cleaned_data['usr']
			passwd = form.cleaned_data['pwd']
			users = Usuario.objects.filter(usuario= user, contrasenna= passwd)
			if(len(users) > 0):
				if(users[0].tipo==1):
					alumno = Alumno.objects.filter(usuario = users[0])
					request.session['ID']= alumno[0].id
					return HttpResponseRedirect('/alumno/main')
				else:
					profesor = Profesor.objects.filter(usuario = users[0])
					request.session['ID']= profesor[0].id
					return HttpResponseRedirect('/profesor/main')
			else:
				form = LoginForm()
				return render(request, 'General/index.html', {'form': form, 'error': 'usuario o contraseña invalidos'})

	else:
		form = LoginForm()
	return render(request, 'General/index.html', {'form': form, 'error': ''})


def ayuda(request):
	return render(request, 'General/ayuda.html', {})

def acercade(request):
	return render(request, 'General/acercade.html', {})

def ayudafile(request):
	print("aloha")
	file= "documentos/mapa-tec.pdf"
	filename = file.split('/')[-1]
	response = HttpResponse(file, content_type='text/plain')
	response['Content-Disposition'] = 'attachment; filename=%s' % filename
	return response