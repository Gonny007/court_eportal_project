# cases/forms.py

from django import forms
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Case, Hearing

class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={'autocomplete': 'off'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'autocomplete': 'off'}),
        required=True
    )

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'autocomplete': 'off'})
    )

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")
        widgets = {
            'username': forms.TextInput(attrs={'autocomplete': 'off'}),
            'email': forms.EmailInput(attrs={'autocomplete': 'off'}),
            'password1': forms.TextInput(attrs={'autocomplete': 'off'}),
            'password2': forms.TextInput(attrs={'autocomplete': 'off'}),
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CaseForm(forms.ModelForm):
    class Meta:
        model = Case
        fields = ['case_number', 'title', 'description', 'date_filed', 'status', 'plaintiff', 'defendant']
        widgets = {
            'date_filed': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_date_filed(self):
        date_filed = self.cleaned_data.get('date_filed')
        if date_filed and date_filed > date.today():
            raise forms.ValidationError("The date filed cannot be in the future.")
        return date_filed

class HearingForm(forms.ModelForm):
    class Meta:
        model = Hearing
        fields = ['case', 'date', 'time', 'description']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }

