# Generated by Django 3.2.8 on 2021-12-05 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('novedades', '0010_alter_novedad_acta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedad',
            name='acta',
            field=models.FileField(blank=True, upload_to='static'),
        ),
    ]
