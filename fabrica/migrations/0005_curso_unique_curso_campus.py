# Generated by Django 5.1.3 on 2024-11-08 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fabrica', '0004_alter_curso_nome'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='curso',
            constraint=models.UniqueConstraint(fields=('nome', 'campus'), name='unique_curso_campus'),
        ),
    ]
