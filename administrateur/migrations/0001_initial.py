# Generated by Django 3.2.3 on 2021-06-07 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='administrateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('prenom', models.CharField(max_length=100, null=True)),
                ('adresse', models.CharField(max_length=100, null=True)),
                ('telephone', models.IntegerField(max_length=12, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('loin', models.CharField(max_length=100, null=True)),
                ('password', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
