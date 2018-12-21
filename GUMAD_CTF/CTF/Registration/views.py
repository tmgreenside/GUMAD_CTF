from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms import formset_factory

from .forms import *
import CTF.models as models

# Create your views here.
def index(request):
    template = loader.get_template('Registration/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def registration(request):
    if request.method == 'POST':
        formTeam = TeamForm(request.POST)
        requiredParticipantForms = formset_factory(ParticipantForm)
        extraParticipantForms = formset_factory(ParticipantForm)

        requiredSetData = {
            'form-TOTAL_FORMS':'3',
            'form-INITIAL_FORMS': '0',
            'form-MAX_NUM_FORMS': ''
        }
        requiredSet = requiredParticipantForms(request.POST, requiredSetData)
        # extraSet = extraParticipantForms(request.POST)
        # check whether it's valid:
        if not formTeam.is_valid():
            message = "Invalid entry. Please try again."
            context = {'formTeam': formTeam, 'memberForm': participantForms, 'message': message}
            return render(request, 'Registration/registrationForm.html', context)
        # for form in participantForms:
        #     if not form.is_valid():
        #         message = "Invalid entry. Please try again."
        #         context = {'formTeam': formTeam, 'memberForm': participantForms, 'message': message}
        #         return render(request, 'Registration/registrationForm.html', context)

        # save team in database
        teamName = formTeam.cleaned_data['name']
        teamInsitition = formTeam.cleaned_data['institution']
        teamLeague = formTeam.cleaned_data['league']
        team = models.Team(name=teamName, institution=teamInsitition, league=teamLeague)
        team.save()

        # save each participant in database
        if requiredSet.is_valid():
            for form in requiredSet:
                firstname = form.cleaned_data['firstname']
                lastname = form.cleaned_data['lastname']
                standing = form.cleaned_data['standing']
                participantTeam = models.Team.object.get(name=teamName)
                newParticipant = models.Participant(firstname=firstname,lastname=lastname,standing=standing,team=participantTeam)
                newParticipant.save()

        # if extraSet.is_valid():
        #     for form in extraSet:
        #         firstname = form.cleaned_data['firstname']
        #         lastname = form.cleaned_data['lastname']
        #         standing = form.cleaned_data['standing']
        #         participantTeam = models.Team.object.get(name=teamName)
        #         newParticipant = models.Participant(firstname=firstname,lastname=lastname,standing=standing,team=participantTeam)
        #         newParticipant.save()

        return HttpResponseRedirect('/Registration')


    # if a GET (or any other method) we'll create a blank form
    else:
        formTeam = TeamForm()
        requiredParticipantForms = formset_factory(ParticipantForm, extra=3)
        extraParticipantForms = formset_factory(ParticipantForm, extra=2, can_delete=True)

    context = {'formTeam': formTeam, 'memberForm': requiredParticipantForms, 'extraForms':extraParticipantForms, 'message': ""}
    return render(request, 'Registration/registrationForm.html', context)

"""
This view displays a form in which users can add their institution if it does not already exist.
"""
def registerInstitution(request):
    if request.method == 'POST':
        form = InstitutionForm(request.POST)
        postURL = "/Registration/RegisterInstitution"

        if form.is_valid():
            # process form data
            name = form.cleaned_data['name']
            city = form.cleaned_data['city']
            state = form.cleaned_data['state']
            country = form.cleaned_data['country']

            submission = models.Institution(name=name,city=city,state=state,country=country)
            submission.save()

            return HttpResponseRedirect('/Registration/Register')
    else:
        form = InstitutionForm()
        postURL = "/Registration/RegisterInstitution"

    return render(request, 'Registration/simpleForm.html', {'postURL': postURL, 'form': form})
