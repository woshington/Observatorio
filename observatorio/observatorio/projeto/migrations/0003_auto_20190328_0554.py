# Generated by Django 2.1.7 on 2019-03-28 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projeto', '0002_projeto_descricao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projeto',
            name='atividades',
            field=models.TextField(blank=True, verbose_name='Atividades'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ciclo_vida',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='projeto.CicloVida', verbose_name='Ciclo de Vida'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='cronograma',
            field=models.FileField(blank=True, upload_to='cronograma/', verbose_name='Cronograma'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_fim',
            field=models.DateTimeField(blank=True, verbose_name='Data do fim'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='data_inicio',
            field=models.DateTimeField(blank=True, verbose_name='Data do inicio'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='descricao',
            field=models.TextField(blank=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='empresa_cliente',
            field=models.CharField(blank=True, max_length=255, verbose_name='Empresa Cliente'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='escopo',
            field=models.TextField(blank=True, verbose_name='Escopo'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='ferramentas',
            field=models.TextField(blank=True, verbose_name='Ferramentas utilizadas para gestão do projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='instituicao',
            field=models.ForeignKey(blank=True, default=False, on_delete=django.db.models.deletion.CASCADE, to='projeto.Instituicao'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='lider_projeto',
            field=models.CharField(blank=True, max_length=255, verbose_name='Líder do Projeto'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='plano_comunicacao',
            field=models.TextField(blank=True, verbose_name='Plano de comunicacao'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='processo_gerenciamento',
            field=models.TextField(blank=True, verbose_name='Processo de gerenciamento de mudanças'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='produtos',
            field=models.TextField(blank=True, verbose_name='Produtos e/ou serviços entregues'),
        ),
        migrations.AlterField(
            model_name='projeto',
            name='riscos',
            field=models.TextField(blank=True, verbose_name='Riscos'),
        ),
    ]