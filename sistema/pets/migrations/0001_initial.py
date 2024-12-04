# Generated by Django 5.1 on 2024-11-28 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('especie', models.CharField(choices=[('cachorro', 'Cachorro'), ('gato', 'Gato'), ('outro', 'Outro')], max_length=50)),
                ('raca', models.CharField(blank=True, max_length=100, null=True)),
                ('idade', models.PositiveIntegerField(blank=True, null=True)),
                ('sexo', models.CharField(choices=[('macho', 'Macho'), ('femea', 'Fêmea'), ('nao_informado', 'Não Informado')], default='nao_informado', max_length=15)),
                ('descricao', models.TextField()),
                ('localizacao', models.CharField(max_length=200)),
                ('data_criacao', models.DateTimeField(auto_now_add=True)),
                ('imagem', models.ImageField(blank=True, null=True, upload_to='pets/')),
            ],
        ),
    ]
