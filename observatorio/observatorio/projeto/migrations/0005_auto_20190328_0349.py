# Generated by Django 2.1.7 on 2019-03-28 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0004_projeto_instituicao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='nome',
            field=models.CharField(max_length=255, unique=True, verbose_name='Nome ou Sigla'),
        ),
    ]
