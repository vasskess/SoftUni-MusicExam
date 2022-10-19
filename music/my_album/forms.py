from django.forms import ModelForm
from django import forms
from music.my_album.models import Album


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = "__all__"
        widgets = {
            "album_name": forms.TextInput(attrs={"placeholder": "Album Name"}),
            "artist": forms.TextInput(attrs={"placeholder": "Artist"}),
            "description": forms.TextInput(attrs={"placeholder": "Description"}),
            "image_url": forms.URLInput(attrs={"placeholder": "Image URL"}),
            "price": forms.TextInput(attrs={"placeholder": "Price"}),
        }


class DeleteAlbum(AlbumForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs["disabled"] = "disabled"
            field.widget.attrs["readonly"] = "readonly"
