from django import forms
from .models import Profile
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    username = forms.CharField(
        help_text=None,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Enter username"}
        ),
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={"class": "form-control", "placeholder": "Enter email"}
        ),
    )

    age = forms.IntegerField(
        required=False,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Enter age"}
        ),
    )

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password"}
        ),
    )

    password2 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Enter password again"}
        ),
    )

    class Meta:
        model = CustomUser
        fields = ("username", "email", "age")

class ProfileForm(forms.ModelForm):

    first_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "First name",
        })
    )

    last_name = forms.CharField(
        max_length=150,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Last name",
        })
    )

    email = forms.EmailField(
        required=False,
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Email address",
        })
    )

    class Meta:
        model = Profile

        fields = [
            "bio",
            "location",
            "profile_picture",
        ]

        widgets = {
            "bio": forms.Textarea(attrs={
                "class": "form-control",
                "rows": 4,
                "placeholder": "Write something about yourself...",
            }),

            "location": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Your location",
            }),

            "profile_picture": forms.ClearableFileInput(attrs={
                "class": "form-control",
            }),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if self.instance and self.instance.pk:
            self.fields["first_name"].initial = (
                self.instance.user.first_name
            )

            self.fields["last_name"].initial = (
                self.instance.user.last_name
            )

            self.fields["email"].initial = (
                self.instance.user.email
            )

    def save(self, commit=True):
        profile = super().save(commit=False)

        profile.user.first_name = self.cleaned_data["first_name"]
        profile.user.last_name = self.cleaned_data["last_name"]
        profile.user.email = self.cleaned_data["email"]

        if commit:
            profile.user.save()
            profile.save()

        return profile
