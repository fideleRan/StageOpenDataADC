# Generated by Django 3.2.13 on 2022-08-22 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0002_delete_journal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_action', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatutJournal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_statut_journal', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StatutTache',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_statut_tache', models.CharField(max_length=50)),
            ],
        ),
    ]
