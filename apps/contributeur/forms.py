from django.forms import ModelForm
from apps.contributeur.models import Journal, ADC, Exclu, Abs_base

class JournalExecutionForm(ModelForm):
    class Meta:
        model = Journal
        fields = '__all__'
        exclude = [
            'nombre_de_page',
            'nombre_ADC',
            'heure_fin',
            'observation',
            # 'nom_journal'
        ]

class JournalExecutionModifForm(ModelForm):
    class Meta:
        model = Journal
        fields = [
            'nombre_de_page',
            'nombre_ADC',
            'heure_fin',
            'observation',
            # 'nom_journal',
            # 'contributeur',
            'statut_journal',
            'jalon'
        ]

class ADCExecutionForm(ModelForm):
    class Meta:
        model = ADC
        fields = '__all__'

class ExcluExecutionForm(ModelForm):
    class Meta:
        model = Exclu
        fields = '__all__'

class ABSBaseExecutionForm(ModelForm):
    class Meta:
        model = Abs_base
        fields = '__all__'

# formulaire multiple