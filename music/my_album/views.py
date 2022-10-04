from django.shortcuts import render


def add_album(request):
    return render(request, "add-album.html")


def album_details(request, pk):
    return render(request, "edit-album.html")


def edit_album(request, pk):
    return render(request, "edit-album.html")


def delete_album(request, pk):
    return render(request, "delete-album.html")
