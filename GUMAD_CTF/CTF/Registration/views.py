from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import *
import CTF.models as models

# Create your views here.
def index(request):
    template = loader.get_template('Registration/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def registration(request):
    # return render(request, 'Registration/registrationForm.html')
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = InstitutionForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/Registration/Thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        formTeam = TeamForm()
        participantForms = [ParticipantForm() for i in range(5)]

    return render(request, 'Registration/registrationForm.html', {'formTeam': formTeam})

# TODO
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
