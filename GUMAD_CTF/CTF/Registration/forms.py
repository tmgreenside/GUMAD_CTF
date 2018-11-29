from django import forms

class TeamRegistration(forms.Form):
    CLASS_STANDINGS = ["Freshman", "Sophomore", "Junior", "Senior"]

    teamname = forms.CharField(label="Your name", max_length=100)
    institutionName = forms.CharField(label="Institution name", max_length=255)

    member1FirstName = forms.CharField(label="Member 1 First Name", max_length=50)
    member1LastName = forms.CharField(label="Member 1 Last Name", max_length=50)
    member1Email = forms.EmailField(label="Member 1 Email")
    member1Year = forms.ChoiceField(choices=CLASS_STANDINGS)

    member2FirstName = forms.CharField(label="Member 2 First Name", max_length=50)
    member2LastName = forms.CharField(label="Member 2 Last Name", max_length=50)
    member2Email = forms.EmailField(label="Member 2 Email")
    member2Year = forms.ChoiceField(choices=CLASS_STANDINGS)

    member3FirstName = forms.CharField(label="Member 3 First Name", max_length=50)
    member3LastName = forms.CharField(label="Member 3 Last Name", max_length=50)
    member3Email = forms.EmailField(label="Member 3 Email")
    member3Year = forms.ChoiceField(choices=CLASS_STANDINGS)

    member4FirstName = forms.CharField(label="Member 4 First Name", max_length=50)
    member4LastName = forms.CharField(label="Member 4 Last Name", max_length=50)
    member4Email = forms.EmailField(label="Member 4 Email")
    member4Year = forms.ChoiceField(choices=CLASS_STANDINGS)

    member5FirstName = forms.CharField(label="Member 5 First Name", max_length=50)
    member5LastName = forms.CharField(label="Member 5 Last Name", max_length=50)
    member5Email = forms.EmailField(label="Member 5 Email")
    member5Year = forms.ChoiceField(choices=CLASS_STANDINGS)
