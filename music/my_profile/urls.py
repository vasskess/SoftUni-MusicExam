from django.urls import path

urlpatterns = (
    path("details/", profile_details, name="profile-details"),
    path("delete/", delete_profile, name="delete-profile"),
)
