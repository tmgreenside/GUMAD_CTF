from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.forms import formset_factory

from django.contrib.auth.hashers import make_password
from django.views.decorators.csrf import csrf_exempt

from .forms import *
import CTF.models as models

# Create your views here.
def index(request):
    template = loader.get_template('Registration/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

"""
If post, process a team registration form. If get, display the form. Input
validation happens both client side and server side for redundancy.
"""
def registration(request):
    if request.method == 'POST':
        formTeam = TeamForm(request.POST)

        if not formTeam.is_valid():
            message = "Invalid entry. Please try again."
            context = {'formTeam': formTeam, 'members': range(5), 'message': message}
            return render(request, 'Registration/registrationForm.html', context)

        passEntry1 = request.POST.get('passentry1')
        passEntry2 = request.POST.get('passentry2')

        if passEntry1 != passEntry2:
            message = "Passwords must match."
            context = {'formTeam': formTeam, 'members': range(5), 'message': message}
            return render(request, 'Registration/registrationForm.html', context)
        elif len(passEntry1) < 8:
            message = "Passwords must be at least ."
            context = {'formTeam': formTeam, 'members': range(5), 'message': message}
            return render(request, 'Registration/registrationForm.html', context)

        # save team in database
        teamName = formTeam.cleaned_data['name']
        teamInsitition = formTeam.cleaned_data['institution']
        teamLeague = formTeam.cleaned_data['league']

        if Team.objects.filter(name=teamName).exists():
            message = "Team name already in use. Please try again."
            context = {'formTeam': formTeam, 'members': range(5), 'message': message}
            return render(request, 'Registration/registrationForm.html', context)

        team = models.Team(name=teamName, institution=teamInsitition, league=teamLeague)

        filled = 0
        for i in range(5):
            items = [request.POST.get('firstname_' + str(i+1)),request.POST.get('lastname_' + str(i+1)),request.POST.get('email_' + str(i+1))]
            partial = False
            for item in items:
                if item != "":
                    partial = True
                elif item == "" and partial == True:
                    message = "Please make sure all required fields are completely filled out."
                    context = {'formTeam': formTeam, 'members': range(5), 'message': message}
                    return render(request, 'Registration/registrationForm.html', context)
            if partial == True:
                filled += 1

        hasUnderclassman = False
        for i in range(filled):
            standing = request.POST.get('standing_' + str(i+1))
            if standing == "Sophomore" or standing == "Freshman":
                hasUnderclassman = True
        if hasUnderclassman == False and filled > 3:
            message = "You can only have more than three teammates if one of them is an underclassman."
            context = {'formTeam': formTeam, 'members': range(5), 'message': message}
            return render(request, 'Registration/registrationForm.html', context)

        password = make_password(passEntry1)
        print("\nPassword:",password)
        print("Length:", len(password), "\n")

        team.save()
        teamLogin = models.TeamLogin(team=team, password=password)
        teamLogin.save()
        participants = []
        for i in range(filled):
            firstname = request.POST.get('firstname_' + str(i+1))
            lastname = request.POST.get('lastname_' + str(i+1))
            email = request.POST.get('email_' + str(i+1))
            if email.rstrip(" ") != "":
                standing = request.POST.get('standing_' + str(i+1))
                participant = models.Participant(firstname=firstname,lastname=lastname,email=email,standing=standing,team=team)
                participants.append(participant)
        for participant in participants:
            participant.save()

        return HttpResponseRedirect('/Registration/ThankYou')

    # if a GET (or any other method) we'll create a blank form
    else:
        formTeam = TeamForm(auto_id="team_%s")

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

"""
This handles an AJAX request to ensure team names are unique.
"""
@csrf_exempt
def checkTeamName(request):
    teamName = request.POST.get('team_name')
    teams = models.Team.objects.filter(name=teamName).count()
    if teams > 0:
        taken = True
    else:
        taken = False
    return render(request, 'Registration/teamNameAvailable.html', {'taken':taken})

"""
This handles an AJAX request to ensure email addresses are unique.
"""
@csrf_exempt
def checkEmail(request):
    address = request.POST.get('address')
    count = models.Participant.objects.filter(email=address).count()
    if count > 0:
        taken = True
    else:
        taken = False
    return render(request, 'Registration/emailAvailable.html', {'taken':taken})



"""
This view displays a page saying "Thank you for registering"
"""
def thanksForRegistering(request):
    return render(request, 'Registration/thanksForRegistering.html')
