# Generated by Django 2.0.3 on 2018-10-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('General', '0007_auto_20181007_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='isrevisado',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
