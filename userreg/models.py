from django.db import models
import random

# Create your models here.

def generateId():
    return random.randint(1,50)*3


class UserDetails(models.Model):
    usr_id = models.IntegerField(null=False, default=generateId(), primary_key=True, unique=True)
    usr_name = models.CharField(max_length=65, null=False)
    eml = models.CharField(max_length=50, null=False, unique=True)
    pss = models.CharField(max_length=12, null=False, unique=True)

    def _str_(self):
        return (self.usr_id+'\n'+self.name+'\n'+self.eml+'\n'+self.pss)