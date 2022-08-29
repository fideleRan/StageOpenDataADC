from django.forms import ModelForm
from apps.contributeur.models import Contributeur
from .models import JournalName

class ContributeurForm(ModelForm):
    class Meta:
        model = Contributeur
        fields = [
            'nom_contributeur',
            'prenom_contributeur',
            'email_contributeur'
        ]

class JournalForm(ModelForm):
    class Meta:
        model = JournalName
        fields = "__all__"