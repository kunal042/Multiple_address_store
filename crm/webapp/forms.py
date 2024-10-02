from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Record

from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

# Register /Create a user

class CreationUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1' , "password2" ]

# Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())



##Create Record 

class CreateRecordForm(forms.ModelForm):

    class Meta:
        model = Record
        # fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', "pincode" ]
        fields = '__all__'

##update Record 

class UpdateRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        # fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'province', "pincode" ]
        fields = '__all__'



