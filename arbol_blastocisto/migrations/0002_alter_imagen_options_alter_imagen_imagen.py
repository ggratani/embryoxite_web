# Generated by Django 4.1.4 on 2023-02-27 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arbol_blastocisto', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='imagen',
            options={'verbose_name': 'embrion', 'verbose_name_plural': 'embriones'},
        ),
        migrations.AlterField(
            model_name='imagen',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='files/embriones'),
        ),
    ]