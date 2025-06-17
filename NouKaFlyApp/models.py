from django.db import models

# Create your models here.
# recherche/models.py

class Recherche(models.Model):
    destination = models.CharField(max_length=100)
    date_depart = models.DateField()
    date_retour = models.DateField()
    date_recherche = models.DateTimeField(auto_now_add=True)