from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        )
    )


class SearchForm(forms.Form):
    query = forms.CharField(label="Search Topic", max_length=100)


class VideoSelectionForm(forms.Form):
    selected_videos = forms.MultipleChoiceField(
        choices=[], widget=forms.CheckboxSelectMultiple, required=False
    )

    def __init__(self, *args, **kwargs):
        videos = kwargs.pop("videos", [])
        super().__init__(*args, **kwargs)
        self.fields["selected_videos"].choices = [
            (str(video["id"]), video["title"]) for video in videos
        ]


class SingleVideoForm(forms.Form):
    video_url = forms.URLField(
        label="YouTube Video URL",
        max_length=200,
        widget=forms.URLInput(attrs={"class": "form-control"}),
    )


from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = UserProfile
        fields = ["bio", "preferred_language", "summary_length"]

    def __init__(self, *args, **kwargs):
        super(UserProfileForm, self).__init__(*args, **kwargs)
        self.fields["email"].initial = self.instance.user.email

    def save(self, commit=True):
        user_profile = super(UserProfileForm, self).save(commit=False)
        user_profile.user.email = self.cleaned_data["email"]
        if commit:
            user_profile.user.save()
            user_profile.save()
        return user_profile
