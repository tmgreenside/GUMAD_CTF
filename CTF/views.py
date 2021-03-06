from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    template = loader.get_template('CTF/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def schedule(request):
    return render(request, 'CTF/schedule.html')

def sponsor(request):
    return render(request, 'CTF/sponsor.html')
