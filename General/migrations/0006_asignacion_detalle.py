# Generated by Django 2.0.3 on 2018-10-06 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0005_auto_20181005_2107'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='detalle',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
