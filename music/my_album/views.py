from django.shortcuts import render


def add_album(request):
    return render(request, "my_album/add-album.html")


def album_details(request, pk):
    return render(request, "my_album/edit-album.html")


def edit_album(request, pk):
    return render(request, "my_album/edit-album.html")


def delete_album(request, pk):
    return render(request, "my_album/delete-album.html")
