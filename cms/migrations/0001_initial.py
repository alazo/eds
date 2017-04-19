# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-19 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=250)),
                ('type', models.CharField(blank=True, default='', max_length=35)),
            ],
            options={
                'verbose_name': 'compétence',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('docfile', models.FileField(upload_to='media/')),
                ('titre', models.CharField(blank=True, max_length=128)),
                ('texte', tinymce.models.HTMLField(blank=True)),
                ('published', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Domaine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigle', models.CharField(blank=True, default='', max_length=5)),
                ('nom', models.CharField(blank=True, default='', max_length=20)),
                ('prenom', models.CharField(blank=True, default='', max_length=20)),
                ('email', models.EmailField(blank=True, default='', max_length=254)),
            ],
            options={
                'ordering': ('nom',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(default='Code', max_length=10)),
                ('nom', models.CharField(default='Nom du module', max_length=100)),
                ('type', models.CharField(choices=[('Spécifique', 'spécifique'), ('Transversal', 'transversal')], max_length=20)),
                ('situation', models.TextField()),
                ('contenu', models.TextField()),
                ('periode_presentiel', models.IntegerField(verbose_name='Période en présentiel')),
                ('travail_perso', models.IntegerField(verbose_name='Travail personnel')),
                ('pratique_prof', models.IntegerField(default=0, verbose_name='Pratique professionnelle')),
                ('didactique', models.TextField()),
                ('evaluation', models.TextField()),
                ('sem1', models.IntegerField(default=0)),
                ('sem2', models.IntegerField(default=0)),
                ('sem3', models.IntegerField(default=0)),
                ('sem4', models.IntegerField(default=0)),
                ('sem5', models.IntegerField(default=0)),
                ('sem6', models.IntegerField(default=0)),
                ('semestre', models.CharField(default='', max_length=15)),
            ],
            options={
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Objectif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('module', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Module')),
            ],
        ),
        migrations.CreateModel(
            name='Processus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=200)),
                ('description', models.TextField(default='')),
                ('domaine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Domaine')),
            ],
            options={
                'verbose_name_plural': 'processus',
                'ordering': ('code',),
            },
        ),
        migrations.CreateModel(
            name='Ressource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('type', models.CharField(choices=[('Savoir', 'savoir'), ('Savoir méthodologique', 'savoir méthodologique'), ('Savoir relationnel', 'savoir relationnel')], default='Savoir', max_length=30)),
                ('module', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Module')),
            ],
        ),
        migrations.CreateModel(
            name='SousCompetence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=20)),
                ('nom', models.CharField(max_length=250)),
                ('competence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cms.Competence')),
            ],
            options={
                'verbose_name': 'sous-compétence',
                'ordering': ('code',),
            },
        ),
        migrations.AddField(
            model_name='module',
            name='processus',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='cms.Processus'),
        ),
        migrations.AddField(
            model_name='domaine',
            name='responsable',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Enseignant'),
        ),
        migrations.AddField(
            model_name='competence',
            name='module',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Module'),
        ),
        migrations.AddField(
            model_name='competence',
            name='proces_eval',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Processus'),
        ),
    ]
