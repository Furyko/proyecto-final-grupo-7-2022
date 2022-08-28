# Generated by Django 4.1 on 2022-08-26 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_fecha_nacimiento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='usuario',
            name='nacimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]