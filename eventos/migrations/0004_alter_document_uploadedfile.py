# Generated by Django 4.1 on 2022-08-28 03:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0003_filesadmin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.FileField(upload_to='media'),
        ),
    ]
