# Generated by Django 2.1.7 on 2019-03-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0005_projeto_ciclo_vida'),
    ]

    operations = [
        migrations.AddField(
            model_name='projeto',
            name='plano_comunicacao',
            field=models.FileField(blank=True, upload_to='plano_comunicacao/', verbose_name='Plano de comunicacao'),
        ),
    ]