from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class AdminLoginForm(forms.Form):

    password = forms.CharField()

    def clean(self):

    	data = super().clean()
    	admin = authenticate(username="admin",password=data.get('password'))

    	if admin is None:

    		raise forms.ValidationError("Incorrect password. Please try again.")

    	return data

    def get_password(self):

    	return self.cleaned_data['password']