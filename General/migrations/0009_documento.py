# Generated by Django 2.0.3 on 2018-10-14 00:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0008_asignacion_isrevisado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
                ('asignacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='General.Asignacion')),
            ],
        ),
    ]
