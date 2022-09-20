from django.forms import ModelForm
from .models import UploadImage
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class Upload(ModelForm):
    class Meta:
        model = UploadImage
        fields = ['author','caption','image','hot','n_not','follower','unfollower']





