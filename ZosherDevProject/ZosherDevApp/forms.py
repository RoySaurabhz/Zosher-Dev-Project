from django import forms
from django.contrib.auth.models import User
from ZosherDevApp.models import UserProfInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfInfoForm(forms.ModelForm):
        class Meta():
            model = UserProfInfo
            fields = ('portfolio_site','profile_pic')
