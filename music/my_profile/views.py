from django.shortcuts import render


def home_page(request):
    return render(request, "my_profile/home-with-profile.html")


def profile_details(request):
    return render(request, "my_profile/profile-details.html")


def delete_profile(request):
    return render(request, "my_profile/profile-delete.html")
