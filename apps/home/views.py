# -*- encoding: utf-8 -*-


from multiprocessing import context
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render




@login_required(login_url="/login/")
# ---------------- ADMIN USER ----------------- #
# views Admin
    # views Accueil_admin
def index(request):
    context = {'segment': 'index'}
    html_template = loader.get_template('home/Accueil.html')
    return HttpResponse(html_template.render(context, request))

    # View Journal_admin
def journal(request) :
    # #Ajout journal
    # context = {'jrnl', 'journal'}
    # html_template = loader.get_template('home/Journal.html')
    # return HttpResponse(html_template.render(context, request))
    
    return render(request, 'home/Journal.html')

    # View Contributeur_admin
def contributeur(request) :
    context = {'contib' : 'contributeur'}
    html_template = loader.get_template('home/Contributeur.html')
    return HttpResponse(html_template.render(context, request))
    # View Recapitulation_admin
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
