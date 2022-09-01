from django.shortcuts import render
from .models import JournalName

# Create your views here.
def accuiel_contributeur(request): #?
    return render(request, "contributeur/Utilisateur.html")

def traitement_contributeur(request):
    journals = JournalName.objects.all()
    context = {
        'journals' : journals
    }

    return render(request, "contributeur/Traitement.html", context )

def execution_contributeur(request):
    return render(request, "contributeur/Execution.html")

def affiche_contributeur(request):
    return render(request, "contributeur/Affichage.html")