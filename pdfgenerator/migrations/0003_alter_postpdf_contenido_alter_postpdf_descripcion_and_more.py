# Generated by Django 4.1.1 on 2022-11-03 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdfgenerator', '0002_alter_postpdf_contenido_alter_postpdf_descripcion_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postpdf',
            name='contenido',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='postpdf',
            name='descripcion',
            field=models.CharField(blank=True, max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='postpdf',
            name='titulo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]