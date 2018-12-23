from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/Register', views.registration, name='Register'),
    path('/RegisterInstitution', views.registerInstitution, name='registerInstitution'),
    path('/ThankYou', views.thanksForRegistering, name='thanksForRegistering')
]
