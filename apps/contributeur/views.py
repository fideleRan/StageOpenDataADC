from django.shortcuts import redirect, render
from .models import JournalName, StatutJournal, Journal, ADC
from .forms import (
    ABSBaseExecutionForm, 
    JournalExecutionForm, 
    ADCExecutionForm, 
    ExcluExecutionForm, 
    JournalExecutionModifForm
    )
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="authentificaton")
def accuiel_contributeur(request): #?
    contributeur = request.user.contributeur
    journals = Journal.objects.all().filter(contributeur=contributeur).order_by('date_heure_debut').reverse()

    paginator = Paginator(journals, 10)
    page = request.GET.get('page')
    journals = paginator.get_page(page)

    context = {
        "journals" : journals
    }
    
    
    print(request.user.contributeur)

    return render(request, "contributeur/Utilisateur.html", context)

@login_required(login_url="authentificaton")
def traitement_contributeur(request):
    journals = JournalName.objects.all()
    journals_traites = Journal.objects.values_list()
    journals_traites = Journal.objects.filter(statut_journal=2) 
    print(journals_traites)

    journals_en_cours = Journal.objects.filter(statut_journal=1)
    
    
    listeJournal = []
    for j in journals:
        listeJournal.append(j)
    
    context = {
        # 'formJournal' : formJournal,
        'journals' : listeJournal,
        'journals_traites' : journals_traites,
        'journals_en_cours' : journals_en_cours
    }

    return render(request, "contributeur/Traitement.html", context )

@login_required(login_url="authentificaton")
def execution_contributeur(request, pk):
    journalName = JournalName.objects.get(id=pk)
    statut_journals = StatutJournal.objects.all()
    statut_journals_default = StatutJournal.objects.get(nom_statut_journal='en saisi')
    journals_get = None
    formADC = ADCExecutionForm()
    formJournal = JournalExecutionForm()
    
    formJournalModif = JournalExecutionModifForm()
    

    formJournal.fields['nom_journal'].initial = journalName
    formJournal.fields['contributeur'].initial = request.user.contributeur
    formJournal.fields['statut_journal'].initial = statut_journals_default
    
    if request.method == 'POST' and 'buttonformJouranl' in request.POST: 
        print("buttonformJournal")
        formJournal = JournalExecutionForm(request.POST)
        if formJournal.is_valid():
            formJournal.save()
            print("save")
            
            if Journal.objects.all()[len(Journal.objects.all()) - 1].nom_journal == journalName:
                journals_get = Journal.objects.all()[len(Journal.objects.all()) - 1]
                # return redirect("execution_user_url")
                print(journals_get.id)
        else:
            print("unsave")
        
    

    if journals_get is not None:
            formADC.fields['reference_ADC'].initial = "{} ADC/{}".format(journalName, journals_get.id) 
            formADC.fields['journal'].initial = journals_get
    

    if request.method == "POST" and 'buttonformADC' in request.POST:
        print("buttonformADC")
        formADC = ADCExecutionForm(request.POST)
        if formADC.is_valid():
            formADC.save()
            print("save adc")
            return redirect("execution_modif")
            
        else:
            print("unsave adc")
        

    context = {
        'journalName' : journalName,
        'statut_journals' : statut_journals,
        'formJournal' : formJournal,
        'formADC' : formADC,
        'journal_get' : journals_get,
        'formJournalModif' : formJournalModif
    }

    return render(request, "contributeur/Execution.html", context)


@login_required(login_url="authentificaton")
def execution_modif(request):
    journals = Journal.objects.all()[len(Journal.objects.all()) - 1]
    journal_modif = Journal.objects.get(id=journals.id)
    statut_journals = StatutJournal.objects.all()
    adcs = ADC.objects.all()[len(ADC.objects.all()) - 1]
    adc_get = ADC.objects.get(id=adcs.id)

    formExclu = ExcluExecutionForm()
    formABS_base = ABSBaseExecutionForm()
    formModif = JournalExecutionModifForm()
    if journals.heure_fin is None and journals.nom_journal == journal_modif.nom_journal \
        and adc_get.reference_ADC == "{} ADC/{}".format(journal_modif.nom_journal, journals.id):

        formModif = JournalExecutionModifForm(instance=journal_modif)
        formABS_base.fields['adc'].initial = adc_get
        formExclu.fields['adc'].initial = adc_get
        if request.method == 'POST' and 'modification' in request.POST:
            formModif = JournalExecutionModifForm(request.POST, instance=journal_modif)
            formExclu = ExcluExecutionForm(request.POST)
            formABS_base = ABSBaseExecutionForm(request.POST)
            if formModif.is_valid() and formABS_base.is_valid() and formExclu.is_valid():
                formModif.save()
                formABS_base.save()
                formExclu.save()
                print("savwe ")
                return redirect("accueil_user_url")

    context = {
        "journal_modif" : journal_modif,
        "statut_journals" : statut_journals,
        "formModif" : formModif,
        'formExclu' : formExclu,
        'formABS_base' : formABS_base
    }

    return render(request, 'contributeur/Execution_modif.html', context)

@login_required(login_url="authentificaton")
def affiche_contributeur(request):
    return render(request, "contributeur/Affichage.html")