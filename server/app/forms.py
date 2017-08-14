from django import forms

class MeetingGalleryForm(forms.Form):
    pictures = forms.ModelChoiceField(queryset=Pictures.object.filter(category=1).order_by('name'))
