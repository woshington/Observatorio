# Generated by Django 2.1.7 on 2019-03-28 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0009_auto_20190328_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(verbose_name='Descrição'),
        ),
    ]
