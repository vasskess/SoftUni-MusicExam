from django.forms import ModelForm

from music.my_profile.models import Profile


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
