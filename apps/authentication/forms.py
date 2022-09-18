from apps.contributeur.models import Contributeur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.forms import ModelForm


User = get_user_model()

class InscriptionForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username', 
            'password1', 
            'password2', 
            'is_adminUser', 
            'contributeur',
            'last_name',
            'first_name',
            'email',
        ]


class SetContributeurHaveAccountTrue(ModelForm):
    class Meta:
        model = Contributeur
        fields = ['have_account']