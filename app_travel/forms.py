from django.forms import ModelForm
from app_travel.models import *

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']