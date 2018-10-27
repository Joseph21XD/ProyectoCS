# Generated by Django 2.0.3 on 2018-10-04 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0002_curso_grupo_logro_logro_estudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asignacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('valor_porcentual', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Asistencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asistio', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Estudiante_Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Alumno')),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=25)),
                ('valor_porcentual', models.FloatField()),
                ('grupo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Grupo')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluacion_Estudiante_Grupo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.IntegerField()),
                ('alumno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Estudiante_Grupo')),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Asignacion')),
            ],
        ),
        migrations.AddField(
            model_name='asistencia',
            name='alumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Estudiante_Grupo'),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='evaluacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Evaluacion'),
        ),
    ]