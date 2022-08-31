from django.shortcuts import render

# Create your views here.
def accuiel_contributeur(request): #?
    return render(request, "contributeur/Utilisateur.html")

def traitement_contributeur(request):
    return render(request, "contributeur/Traitement.html")

def execution_contributeur(request):
    return render(request, "contributeur/Execution.html")

def affiche_contributeur(request):
    return render(request, "contributeur/Affichage.html")