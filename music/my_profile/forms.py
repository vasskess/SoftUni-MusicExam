from django import forms
from django.forms import ModelForm

from music.my_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        widgets = {
            "username": forms.TextInput(attrs={"placeholder": "Username"}),
            "email": forms.TextInput(attrs={"placeholder": "Email"}),
            "age": forms.TextInput(attrs={"placeholder": "Age"}),
        }
