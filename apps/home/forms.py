from django.forms import ModelForm
from apps.contributeur.models import Contributeur

class ContributeurForm(ModelForm):
    class Meta:
        model = Contributeur
        fields = [
            'nom_contributeur',
            'prenom_contributeur',
            'email_contributeur'
        ]