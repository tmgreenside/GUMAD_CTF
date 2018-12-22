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

    # look at redoing using a raw form
    if request.method == 'POST':
        formTeam = TeamForm(request.POST)

        if not formTeam.is_valid():
            message = "Invalid entry. Please try again."
            context = {'formTeam': formTeam, 'memberForm': participantForms, 'message': message}
            return render(request, 'Registration/registrationForm.html', context)

        # save team in database
        teamName = formTeam.cleaned_data['name']
        teamInsitition = formTeam.cleaned_data['institution']
        teamLeague = formTeam.cleaned_data['league']
        team = models.Team(name=teamName, institution=teamInsitition, league=teamLeague)
        team.save()

        for i in range(3):
            items = [request.POST.get('firstname_' + str(i+1)),request.POST.get('lastname_' + str(i+1)),request.POST.get('email_' + str(i+1))]
            for item in items:
                if item == "":
                    message = "Please make sure all required fields are completely filled out."
                    context = {'formTeam': formTeam, 'members': range(5), 'message': message}
                    return render(request, 'Registration/registrationForm.html', context)

        for i in range(5):
            firstname = request.POST.get('firstname_' + str(i+1))
            lastname = request.POST.get('lastname_' + str(i+1))
            email = request.POST.get('email_' + str(i+1))
            standing = request.POST.get('standing_' + str(i+1))

            participant = models.Participant(firstname=firstname,lastname=lastname,email=email,standing=standing,team=team)
            participant.save()

        return HttpResponseRedirect('/Registration')


    # if a GET (or any other method) we'll create a blank form
    else:
        formTeam = TeamForm()

    # TODO: add extra forms
    context = {'formTeam': formTeam, 'members': range(5), 'message': ""}
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
