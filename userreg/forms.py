from .models import UserDetails
from django.forms import ModelForm


class UsrRegForm(ModelForm):
     class Meta:
         model = UserDetails
         exclude = ['usr_id']