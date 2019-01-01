from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Schedule', views.schedule, name='schedule'),
    path('Sponsor', views.sponsor, name='sponsor'),
    path('Registration', include('CTF.Registration.urls')),
]
