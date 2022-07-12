from django import forms
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import *
from .models import *
from .views import *
from django import forms




class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=120)
    password = forms.CharField(max_length=15)

    class Meta:
        fields = ("__all__")

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = Userprof
        fields = ("__all__")

class PoolForm(forms.Form):
    Source = forms.CharField(max_length=200)
    Destination = forms.CharField(max_length=200)
    # date = forms.DateTimeField()

    class Meta:
        fields = ("__all__")


class DriverRegistrationForm(forms.ModelForm):

    class Meta:
        model = Driver
        fields = ("__all__")




