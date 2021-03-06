from django import forms
from CTF.models import Institution, Team, Participant

CLASS_STANDINGS = ["Freshman", "Sophomore", "Junior", "Senior"]
LEAGUES = ["Canary", "Swallow"]

class InstitutionForm(forms.ModelForm):
    class Meta:
        model = Institution
        fields = ['name', 'city', 'state', 'country']

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name','institution','league']
        labels = {'name':'Team Name', 'institution':'Institution', 'league':'League'}

class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['firstname','lastname','standing','team']
        exclude = ('team',)
