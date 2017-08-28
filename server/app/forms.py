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


class JoinUsForm(forms.Form):

    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(required=True)
    t_shirt_size = forms.ChoiceField(required=True, choices=(
        (0, 'Small'),
        (1, 'Medium'),
        (2, 'Large'),
        (3, 'Extra Large'),
        ))

    def clean(self):

        data = super().clean()

        return data
