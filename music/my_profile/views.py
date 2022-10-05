

from django.shortcuts import render

from music.my_album.models import Album
from music.my_profile.forms import ProfileForm
from music.my_profile.models import Profile


def home_page(request):
    user = Profile.objects.first()
    if not user:
        form = ProfileForm()
        if request.method == "POST":
            form = ProfileForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request, "my_profile/home-with-profile.html")
        context = {"form": form}
        return render(request, "my_profile/home-no-profile.html", context)
    albums = Album.objects.all()
    context = {"albums": albums}
    return render(request, "my_profile/home-with-profile.html", context)


def profile_details(request):
    return render(request, "my_profile/profile-details.html")


def delete_profile(request):
    return render(request, "my_profile/profile-delete.html")
