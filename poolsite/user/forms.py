from django import forms
from django.contrib.auth import login , authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.conf import *
from .models import *
from .views import *
from django import forms
from .widget import DatePickerInput, TimePickerInput, DateTimePickerInput


class UserLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=15)

    class Meta:
        fields = ("__all__")

    # def clean_email(self):
    #     email = self.cleaned_data.get("email")
    #     password = self.cleaned_data.get("password")
    #     print("\n\n\n\n\n\n\n cleand email ", self)
    #     obj = get_object_or_404(Userprof, password, email)

    #     # raise forms.ValidationError("This title is already been used , pls add another one ")
    #     return self
 

class UserRegistrationForm(forms.ModelForm):

    class Meta:
        model = Userprof
        fields = ("__all__")

        

class PoolForm(forms.Form):
    Source = forms.CharField(max_length=200)
    Destination = forms.CharField(max_length=200)
    my_date_field = forms.DateField(widget=DatePickerInput)
    my_time_field = forms.TimeField(widget=TimePickerInput)
    # date = forms.DateTimeField()

    class Meta:
        fields = ("__all__")


class DriverRegistrationForm(forms.ModelForm):
        my_date_field = forms.DateField(widget=DatePickerInput)
        my_time_field = forms.TimeField(widget=TimePickerInput)
        class Meta:
          model = Driver
          fields = ("__all__")
        

class DriverLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(max_length=15)

    class Meta:
        fields = ("__all__")

