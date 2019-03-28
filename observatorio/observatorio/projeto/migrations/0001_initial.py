# Generated by Django 2.1.7 on 2019-03-27 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instituicao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, unique=True, verbose_name='Instituição')),
                ('cidade', models.CharField(blank=True, max_length=255, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, max_length=2, null=True, verbose_name='UF')),
            ],
            options={
                'verbose_name': 'Instituição',
                'verbose_name_plural': 'Instituições',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='MembroEquipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('funcao', models.CharField(max_length=255, verbose_name='Função')),
            ],
            options={
                'verbose_name': 'Membro da Equipe',
                'verbose_name_plural': 'Membros da Equipe',
                'ordering': ['nome'],
            },
        ),
        migrations.CreateModel(
            name='Projeto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(default=False, max_length=255, unique=True, verbose_name='Nome ou Sigla')),
                ('escopo', models.TextField(verbose_name='Escopo')),
                ('atividades', models.TextField(verbose_name='Atividades')),
                ('produtos', models.TextField(verbose_name='Produtos e/ou serviços entregues')),
                ('orcamento_previsto', models.FloatField(blank=True, default=None, null=True, verbose_name='Orçamento previsto')),
                ('orcamento_executado', models.FloatField(blank=True, default=None, null=True, verbose_name='Orçamento executado')),
                ('data_inicio', models.DateTimeField(verbose_name='Data do inicio')),
                ('data_fim', models.DateTimeField(verbose_name='Data do fim')),
                ('plano_comunicacao', models.TextField(verbose_name='Plano de comunicacao')),
                ('cronograma', models.FileField(upload_to='cronograma/', verbose_name='Cronograma')),
                ('riscos', models.TextField(verbose_name='Riscos')),
                ('ferramentas', models.TextField(verbose_name='Ferramentas utilizadas para gestão do projeto')),
                ('processo_gerenciamento', models.TextField(verbose_name='Processo de gerenciamento de mudanças')),
                ('status', models.CharField(choices=[('0', ''), ('1', 'Concluido'), ('2', 'Em andamento'), ('3', 'Atrasado')], default='0', max_length=1, verbose_name='Status')),
                ('membros', models.ManyToManyField(blank=True, to='projeto.MembroEquipe', verbose_name='Membros')),
            ],
            options={
                'verbose_name': 'Projetos',
                'verbose_name_plural': 'Projetos',
                'ordering': ['nome'],
            },
        ),
    ]
