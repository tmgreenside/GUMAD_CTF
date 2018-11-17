from django.db import models

STATE_CHOICES = ['AK', 'AL', 'AR', 'AZ', 'CA', 'CO', 'CT', 'DC', 'DE', 'FL', 'GA', 'HI', 'IA', 'ID', 'IL', 'IN', 'KS', 'KY',
            'LA', 'MA', 'MD', 'ME', 'MI', 'MN', 'MO', 'MS', 'MT', 'NC', 'ND', 'NE', 'NH', 'NJ', 'NM', 'NV', 'NY', 'OH',
            'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VA', 'VT', 'WA', 'WI', 'WV', 'WY']

CLASS_STANDINGS = ["Freshman", "Sophomore", "Junior", "Senior"]

# Create your models here.
class Institution(models.Model):
    name = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    state_province = models.CharField(max_length=2, choices=STATE_CHOICES, blank=True, null=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=250)
    institution = models.ForeignKey(Institution, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Participant(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=25)
    standing = models.CharField(max_length=20, choices=CLASS_STANDINGS, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.firstname + " " + self.lastname
