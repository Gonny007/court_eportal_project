from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Case, Hearing
from .forms import LoginForm


def case_list(request):
    cases = Case.objects.all()
    return render(request, 'cases/case_list.html', {'cases': cases})

def case_detail(request, case_number):
    case = get_object_or_404(Case, case_number=case_number)
    return render(request, 'cases/case_detail.html', {'case': case})

def hearing_list(request, case_number):
    case = get_object_or_404(Case, case_number=case_number)
    hearings = case.hearings.all()
    return render(request, 'cases/hearing_list.html', {'case': case, 'hearings': hearings})

def frontpage_view(request):
    return render(request, 'cases/index.html')


# cases/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm  # Ensure this import is correct

def login_view(request):
    return render(request, 'cases/login.html')

def register_view(request):
    return render(request, 'cases/register.html')

def about_view(request):
    return render(request, 'cases/about.html')

def contact_view(request):
    return render(request, 'cases/contact.html')

