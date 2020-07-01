from django import forms
from .models import Profile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProfileForm(forms.ModelForm):
    class Meta:
        model   =   Profile
        fields  =   [
            'full_name',
            'address1',
            'address2',
            'locality',
            'region',
            'postal_code',
            'country',
            'phone_number',
            'email',
            'image'
        ]



class SignUpForm(UserCreationForm):
    username = forms.EmailField(max_length=200)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )