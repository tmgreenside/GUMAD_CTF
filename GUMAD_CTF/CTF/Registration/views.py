from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import TeamRegistration

# Create your views here.
def index(request):
    template = loader.get_template('Registration/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TeamRegistration(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/Registration/Thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TeamRegistration()

    return render(request, 'Registration/registrationForm.html', {'form': form})
