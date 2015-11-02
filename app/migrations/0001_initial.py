# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=200)),
                ('apellido_paterno', models.CharField(max_length=200)),
                ('apellido_materno', models.CharField(max_length=200)),
                ('direccion', models.CharField(max_length=250)),
                ('telefono', models.CharField(max_length=250)),
                ('foto', models.ImageField(upload_to=b'persona')),
            ],
            options={
                'verbose_name': 'Persona',
                'verbose_name_plural': 'Personas',
            },
        ),
    ]
