# Generated by Django 4.1 on 2022-08-27 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='categoria_id',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='modalidad_id',
        ),
        migrations.RemoveField(
            model_name='evento',
            name='participantes',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.DeleteModel(
            name='Modalidad',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]
