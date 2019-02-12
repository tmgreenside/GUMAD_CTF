from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/Register', views.registration, name='Register'),
    path('/RegisterInstitution', views.registerInstitution, name='registerInstitution'),
    path('/CheckTeamName', views.checkTeamName, name="checkTeamName"),
    path('/CheckEmail', views.checkEmail, name="checkEmail"),
    path('/ThankYou', views.thanksForRegistering, name='thanksForRegistering')
]
