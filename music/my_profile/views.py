from django.shortcuts import render


def home_page(request):
    return render(request, "home-with-profile.html")


def profile_details(request):
    return render(request, "profile-details.html")


def delete_profile(request):
    return render(request, "profile-delete.html")
