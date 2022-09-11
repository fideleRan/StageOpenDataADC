from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import InscriptionForm
from apps.contributeur.models import Contributeur


def inscription(request, pk):
    contributeur = Contributeur.objects.get(id=pk)
    msg = ""
    form = InscriptionForm()

    form.fields['contributeur'].initial = contributeur
    form.fields['username'].initial = contributeur.nom_contributeur 
    form.fields['last_name'].initial = contributeur.nom_contributeur
    form.fields['first_name'].initial = contributeur.prenom_contributeur
    form.fields['email'].initial = contributeur.email_contributeur

    print(form)
    if request.method == "POST":
        form = InscriptionForm(data=request.POST)  
        if form.is_valid():
            form.save()
            print("save")
            msg = "saved"
            return redirect("/authentification/")
            
        else:
            print("unsave")
            msg = "unsaved"

    context = {
        'form' : form,
        'msg' : msg,
        'contributeur' : contributeur
    }

    return render(request, "accounts/inscription.html", context=context)

def authentification(request):
    error = ""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.is_adminUser:
                return redirect("/adminUser/journal/")
            
            elif user.is_contributeur:
                return redirect("/contributeur/accueil/")

        else:
            error = "Invalide authentication!"

    context = {
        'error' : error
    }

    return render(request, "accounts/authentification.html", context=context)
