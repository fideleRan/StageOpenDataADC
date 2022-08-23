from django.db import models

# Create your models here.
class Action(models.Model):
    nom_action = models.CharField(max_length=50)


class StatutJournal(models.Model):
    nom_statut_journal = models.CharField(max_length=50)


class StatutTache(models.Model):
    nom_statut_tache = models.CharField(max_length=50)


class JournalName(models.Model):
    nom_journal = models.CharField(max_length=50)