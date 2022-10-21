# -*- encoding: utf-8 -*-

from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render, redirect

from apps.home.forms import ContributeurForm, JournalForm, ActionForm, StatutJournalForm, StatutTacheForm
from apps.contributeur.models import Contributeur
from apps.home.models import JournalName, Action, StatutJournal, StatutTache

@login_required(login_url="authentificaton")
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/Accueil.html')
    return HttpResponse(html_template.render(context, request))

    # View Journal_admin
@login_required(login_url="authentificaton")
def journal(request) :
    form = JournalForm()
    if request.method == 'POST':
        print("request post")
        form = JournalForm(request.POST)
        if form.is_valid():
            form.save()
            print("save journal")
            return redirect("/adminUser/journal/")
        else:
            print("unsave journal")

    journals = JournalName.objects.all()

    context = {
        'form' : form,
        'journals' : journals
    }

    return render(request, 'home/Journal.html', context=context)

@login_required(login_url="authentificaton")
def contributeur(request) :
    form = ContributeurForm()
    if request.method == 'POST':
        form = ContributeurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminUser/contributeur/")

    contributeurs = Contributeur.objects.all()

    context = {
        'contib' : 'contributeur',
        'form' : form,
        'contributeurs' : contributeurs
    }
    html_template = loader.get_template('home/Contributeur.html')
    return HttpResponse(html_template.render(context, request))
    # View Recapitulation_admin

@login_required(login_url="authentificaton")
def action(request):
    form = ActionForm()
    if request.method == "POST":
        form = ActionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminUser/action/")

    actions = Action.objects.all()

    context = {
        'form' : form,
        'actions' : actions
    }

    return render(request, "home/action.html", context)

@login_required(login_url="authentificaton")
def statut_journal(request):
    form = StatutJournalForm()
    if request.method == "POST":
        form = StatutJournalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminUser/statutJournal/")

    statut_journals = StatutJournal.objects.all()

    context = {
        'form' : form,
        'statut_journals' : statut_journals
    }
    return render(request, "home/statut_journal.html", context)

@login_required(login_url="authentificaton")
def statut_tache(request):
    form = StatutTacheForm()
    if request.method == "POST":
        form = StatutTacheForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/adminUser/statutTache/")

    statut_taches = StatutTache.objects.all()

    context = {
        'form' : form,
        'statut_taches' : statut_taches
    }

    return render(request, "home/statut_tache.html", context)

@login_required(login_url="authentificaton")
def recapitulation(request) :
    context = {'recap' : 'recapitulation'}
    html_template = loader.get_template('home/Recapitulation.html')
    return HttpResponse(html_template.render(context, request))


# -------------- SIMPLE USER -------------- #
# View Utilisateur simple
    # Accueil USER
# def utilisateur(request) :
#     context = {'utilisateur' : 'utilisateur'}
#     html_template = loader.get_template('contributeur/Utilisateur.html')
#     return HttpResponse(html_template.render(context, request))
#     # Traitement USER
# def traitement_user(request) :
#     context = {'traitement' : 'traitement'}
#     html_template = loader.get_template('contributeur/Traitement.html')
#     return HttpResponse(html_template.render(context, request))    
#     # Execution USER
# def execution_user(request) :
#     context = {'execution' : 'execution'}
#     html_template = loader.get_template('contributeur/Execution.html')
#     return HttpResponse(html_template.render(context, request)) 
#     # Afficher les information de journal traité 
# def affichage_user(request):
#     context = {'afficheer' : 'afficher'}
#     html_template = loader.get_template('contributeur/Affichage.html')
#     return HttpResponse(html_template.render(context, request)) 
#     #Rapport personnel de l'utilisateur simple
def rapport_user(request):
    context={'rapport' : 'rapport'}
    html_template = loader.get_template('contributeur/Rapport_user.html')
    return HttpResponse(html_template.render(context, request))
    
    
@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

def profil_info(request):
    return render(request, 'home/profile.html')