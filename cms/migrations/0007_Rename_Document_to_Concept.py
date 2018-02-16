# Generated by Django 2.0.1 on 2018-02-16 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_auto_20170616_0906'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Document',
            new_name='Concept',
        ),
        migrations.RemoveField(
            model_name='module',
            name='periode_presentiel',
        ),
        migrations.AlterField(
            model_name='competence',
            name='module',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Module'),
        ),
        migrations.AlterField(
            model_name='competence',
            name='proces_eval',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Processus'),
        ),
        migrations.AlterField(
            model_name='domaine',
            name='responsable',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Enseignant'),
        ),
        migrations.AlterField(
            model_name='module',
            name='processus',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Processus'),
        ),
        migrations.AlterField(
            model_name='objectif',
            name='module',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='cms.Module'),
        ),
        migrations.AlterField(
            model_name='processus',
            name='domaine',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Domaine'),
        ),
        migrations.AlterField(
            model_name='ressource',
            name='module',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to='cms.Module'),
        ),
        migrations.AlterField(
            model_name='souscompetence',
            name='competence',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Competence'),
        ),
        migrations.AlterField(
            model_name='uploaddoc',
            name='docfile',
            field=models.FileField(upload_to='doc'),
        ),
    ]
