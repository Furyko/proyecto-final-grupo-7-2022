# Generated by Django 4.1 on 2022-08-26 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_remove_usuario_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='nacimiento',
            field=models.DateField(blank=True, null=True, verbose_name=('%d-%m-%Y', '%Y-%m-%d')),
        ),
    ]
