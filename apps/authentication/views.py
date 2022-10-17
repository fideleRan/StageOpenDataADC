from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import InscriptionForm, SetContributeurHaveAccountTrue
from apps.contributeur.models import Contributeur


def inscription(request, pk):
    contributeur = Contributeur.objects.get(id=pk)
    msg = ""
    form = InscriptionForm()
    set_have_account_true = SetContributeurHaveAccountTrue(instance=contributeur)

    set_have_account_true.fields['have_account'].initial = True

    form.fields['contributeur'].initial = contributeur
    form.fields['username'].initial = contributeur.nom_contributeur 
    form.fields['last_name'].initial = contributeur.nom_contributeur
    form.fields['first_name'].initial = contributeur.prenom_contributeur
    form.fields['email'].initial = contributeur.email_contributeur

    # print(contributeur.have_account)
    # print(set_have_account_true)
    if request.method == "POST":
        form = InscriptionForm(data=request.POST)  
        set_have_account_true = SetContributeurHaveAccountTrue(request.POST, instance=contributeur)
        if form.is_valid() and set_have_account_true.is_valid():
            form.save()
            set_have_account_true.save()
            print(contributeur.have_account)
            print("save")
            msg = "saved"
            return redirect("/authentification/")
            
        else:
            print("unsave")
            msg = "unsaved"

    context = {
        'form' : form,
        'msg' : msg,
        'contributeur' : contributeur,
        'set_have_account_true' : set_have_account_true
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

def logoutUser(request):
    logout(request)
    return redirect("authentificaton")
