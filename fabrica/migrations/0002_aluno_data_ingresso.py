# Generated by Django 5.1.2 on 2024-11-04 20:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aluno',
            name='data_ingresso',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
