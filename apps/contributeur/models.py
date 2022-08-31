from django.db import models
from apps.home.models import Action, StatutJournal, StatutTache, JournalName

# Create your models here.
class Contributeur(models.Model):
    nom_contributeur = models.CharField(max_length=30)
    prenom_contributeur = models.CharField(max_length=50)
    email_contributeur = models.EmailField(max_length=30)

    action_contributeur = models.ForeignKey(Action, on_delete=models.SET_NULL, null=True) 


class Journal(models.Model):
    #edition = models.PositiveSmallIntegerField()
    nom_journal = models.ForeignKey(JournalName, on_delete=models.CASCADE) # !
    nombre_de_page = models.PositiveSmallIntegerField() 
    nombre_ADC = models.PositiveSmallIntegerField(default=0)
    date_heure_debut = models.DateTimeField(auto_now_add=True)
    heure_fin = models.TimeField(auto_now=False, auto_now_add=False)
    observation = models.TextField(null=True, blank=True)

    contributeur = models.ForeignKey(Contributeur, on_delete=models.CASCADE, null=True)
    statut_journal = models.ForeignKey(StatutJournal, on_delete=models.SET_NULL , null=True)


class ADC(models.Model):
    nom_ADC = models.CharField(max_length=50)

    journal = models.ForeignKey(Journal, on_delete=models.CASCADE, null=True)


class Exclu(models.Model):
    additif_rectificatif_erratum_modif = models.PositiveSmallIntegerField(default=0)
    doublon = models.PositiveSmallIntegerField(default=0)
    exclu_ceremonie = models.PositiveSmallIntegerField(default=0)
    aucun_ville = models.PositiveSmallIntegerField(default=0)
    nombre_exclu = None

    adc = models.ForeignKey(ADC, on_delete=models.CASCADE, null=True)


class Abs_base(models.Model):
    ads_dans_la_base = models.PositiveSmallIntegerField(default=0)
    repos = models.PositiveSmallIntegerField(default=0)
    nombre_abs = None

    adc = models.ForeignKey(ADC, on_delete=models.CASCADE, null=True)


class Tache(models.Model):
    nom_tache = models.CharField(max_length=30) #<choices
    date_heure_debut_tache = models.DateTimeField(auto_now_add=True)
    heure_fin_tache = models.TimeField(auto_now=False, auto_now_add=False)
    observation_tache = models.TextField(null=True, blank=True) 

    contributeur = models.ForeignKey(Contributeur, on_delete=models.CASCADE, null=True)
    statut_tache = models.ForeignKey(StatutTache, on_delete=models.SET_NULL, null=True)
