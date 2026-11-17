
from django.urls import path
from . import views
from .views import SignUpView

app_name = "accounts"

urlpatterns = [
    path(
        "signup/",
        SignUpView.as_view(),
        name="signup"
    ),

    path(
        "profile/",
        views.profile_view,
        name="profile"
    ),

    path(
        "profile/edit/",
        views.profile_edit,
        name="profile_edit"
    ),
]
