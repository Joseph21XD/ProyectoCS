from django.db import models

class Usuario(models.Model):
	usuario = models.CharField(max_length=25)
	contrasenna=	models.CharField(max_length=25)
	tipo = models.IntegerField()
	def __str__(self):
            return self.usuario


class Profesor(models.Model):
	nombre = models.CharField(max_length=20)
	apellido1 = models.CharField(max_length=20)
	apellido2 = models.CharField(max_length=20)
	correo=	models.CharField(max_length=60)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	avatar= models.CharField(max_length=100)
	def __str__(self):
            return self.nombre +" "+ self.apellido1 +" "+ self.apellido2

class Alumno(models.Model):
	nombre = models.CharField(max_length=20)
	apellido1 = models.CharField(max_length=20)
	apellido2 = models.CharField(max_length=20)
	carnet=	models.CharField(max_length=20)
	nickname= models.CharField(max_length=20)
	avatar= models.CharField(max_length=100)
	usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	def __str__(self):
            return self.nombre +" "+ self.apellido1 +" "+ self.apellido2

class Curso(models.Model):
	nombre = models.CharField(max_length=25)
	def __str__(self):
            return self.nombre

class Grupo(models.Model):
	anno = models.CharField(max_length=4)
	seccion = models.CharField(max_length=5)
	periodo = models.CharField(max_length=20)
	grado=	models.IntegerField()
	profesorGuia = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name = "ProfesorGuia")
	profesor = models.ForeignKey(Profesor, on_delete=models.CASCADE, related_name = "Profesor")
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
	def __str__(self):
            return self.curso.__str__()+"-"+ str(self.grado)+"-"+self.seccion+"-"+self.anno

class Logro(models.Model):
	nombre = models.CharField(max_length=25)
	descripcion = models.CharField(max_length=100)
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	def __str__(self):
            return self.nombre+"-"+self.grupo.__str__()

class Logro_Estudiante(models.Model):
	alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
	logro = models.ForeignKey(Logro, on_delete=models.CASCADE)
	def __str__(self):
            return self.alumno.__str__()+"-"+self.logro.__str__()

class Evaluacion(models.Model):
	nombre = models.CharField(max_length=25)
	valor_porcentual = models.FloatField()
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	def __str__(self):
            return self.nombre+"-"+self.grupo.__str__()

class Asignacion(models.Model):
	nombre = models.CharField(max_length=25)
	valor_porcentual = models.FloatField()
	detalle = models.CharField(max_length=100, blank = True )
	evaluacion = models.ForeignKey(Evaluacion, on_delete=models.CASCADE)
	fecha = models.DateField()
	fechaFinal = models.DateField(null = True)
	isrevisado = models.IntegerField()
	def __str__(self):
            return self.nombre+"-"+self.evaluacion.__str__()

class Estudiante_Grupo(models.Model):
	alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
	grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
	nota = models.IntegerField()
	def __str__(self):
            return self.alumno.nombre+"-"+self.grupo.seccion+"-"+ str(self.grupo.grado)

class Asistencia(models.Model):
	alumno = models.ForeignKey(Estudiante_Grupo, on_delete=models.CASCADE)
	asistio = models.IntegerField()
	fecha = models.DateField()
	def __str__(self):
            return self.alumno.__str__()+"-"+self.fecha.strftime('%Y-%m-%d') 

class Evaluacion_Estudiante_Grupo(models.Model):
	alumno = models.ForeignKey(Estudiante_Grupo, on_delete=models.CASCADE)
	asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
	nota = models.IntegerField()
	def __str__(self):
            return self.alumno.__str__()+"-"+self.asignacion.__str__()

class Documento(models.Model):
 filename = models.CharField(max_length=100)
 docfile = models.FileField(upload_to='documents')
 asignacion = models.ForeignKey(Asignacion, on_delete=models.CASCADE)
