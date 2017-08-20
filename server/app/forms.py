from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class ContactUsForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    message = forms.CharField(required=True)

    def clean(self):

    	data = super().clean()

    	return data
