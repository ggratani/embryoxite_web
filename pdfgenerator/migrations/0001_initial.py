# Generated by Django 4.1.1 on 2022-11-03 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Postpdf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=500)),
                ('contenido', models.CharField(max_length=500)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='blog')),
                ('descripcion', models.CharField(max_length=5000)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'postpdf',
                'verbose_name_plural': 'postpdfs',
            },
        ),
    ]