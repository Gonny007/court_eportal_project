# cases/forms.py
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, required=True)
    password = forms.CharField(widget=forms.PasswordInput, required=True)

from django import forms
from django.contrib.auth.forms import UserCreationForm
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
    

from django import forms
from .models import Case, Hearing

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_number', 'title', 'description', 'date_filed', 'status']
        widgets = {
            'date_filed': forms.DateInput(attrs={'type': 'date'}),
        }

class HearingForm(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = ['case', 'date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

