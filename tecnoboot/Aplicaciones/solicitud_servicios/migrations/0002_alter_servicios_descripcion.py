# Generated by Django 4.1.1 on 2022-10-10 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solicitud_servicios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicios',
            name='descripcion',
            field=models.TextField(),
        ),
    ]
