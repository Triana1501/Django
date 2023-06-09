# Generated by Django 3.2.7 on 2023-05-11 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portafolio', '0002_alter_project_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='actualizar',
            field=models.DateTimeField(auto_now=True, verbose_name='fecha actualizar'),
        ),
        migrations.AlterField(
            model_name='project',
            name='crear',
            field=models.DateTimeField(auto_now_add=True, verbose_name='fecha crear'),
        ),
        migrations.AlterField(
            model_name='project',
            name='descripcion',
            field=models.TextField(verbose_name='descripcion'),
        ),
        migrations.AlterField(
            model_name='project',
            name='imagen',
            field=models.ImageField(upload_to='project', verbose_name='imagen'),
        ),
        migrations.AlterField(
            model_name='project',
            name='titulo',
            field=models.CharField(max_length=50, verbose_name='titulo'),
        ),
    ]
