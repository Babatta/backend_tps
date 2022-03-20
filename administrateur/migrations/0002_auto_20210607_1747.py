# Generated by Django 3.2.3 on 2021-06-07 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('utilisateur', '0001_initial'),
        ('administrateur', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='administrateur',
            name='adresse',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='email',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='loin',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='nom',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='password',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='prenom',
        ),
        migrations.RemoveField(
            model_name='administrateur',
            name='telephone',
        ),
        migrations.AddField(
            model_name='administrateur',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='utilisateur.utilisateur'),
        ),
    ]