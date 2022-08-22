from django.db import models

# Create your models here.
class Contributeur(models.Model):
    nom_contributeur = models.CharField(max_length=50)
    prenom_contributeur = models.CharField(max_length=100)
    email_contributeur = models.EmailField(max_length=50)


class Journal(models.Model):
    edition = models.PositiveSmallIntegerField()
    nom_journal = models.CharField(max_length=50)
    nombre_de_page = models.PositiveSmallIntegerField() 
    nombre_ADC = models.PositiveSmallIntegerField(default=0)
    date_heure_debut = models.DateTimeField(auto_now=True, auto_now_add=True)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)
    observation = models.TextField(null=True, blank=True)


class ADC(models.Model):
    nom_ADC = models.CharField(max_length=50)


class Exclu(models.Model):
    additif_rectificatif_erratum_modif = models.PositiveSmallIntegerField(default=0)
    doublon = models.PositiveSmallIntegerField(default=0)
    exclu_ceremonie = models.PositiveSmallIntegerField(default=0)
    aucun_ville = models.PositiveSmallIntegerField(default=0)
    nombre_exclu = None


class Abs_base(models.Model):
    ads_dans_la_base = models.PositiveSmallIntegerField(default=0)
    repos = models.PositiveSmallIntegerField(default=0)
    nombre_abs = None


class Tache(models.Model):
    nom_tache = models.CharField(max_length=50) #<choices
    date_heure_debut_tache = models.DateTimeField(auto_now=True, auto_now_add=True)
    heure_fin_tache = models.TimeField(auto_now=False, auto_now_add=False)
    observation_tache = models.TextField(null=True, blank=True) 
