from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login
from .models import Case, Hearing
from .forms import LoginForm
from django.contrib import messages



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

# def register_view(request):
#     return render(request, 'cases/register.html')

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login')  # Redirect to the login page
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

    return render(request, 'register.html', {'form': form})


def about_view(request):
    return render(request, 'cases/about.html')

def contact_view(request):
    return render(request, 'cases/contact.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('case_list')  # Use the name of the URL pattern for the case list
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')

# --------------------------------------------------------------------------------------------------------
from django.shortcuts import render, redirect, get_object_or_404
from .models import Case, Hearing
from .forms import CaseForm, HearingForm
from django.contrib.auth.decorators import login_required

@login_required

def case_list_view(request):
    cases = Case.objects.all()
    return render(request, 'cases/case_list.html', {'cases': cases})

@login_required

def case_create_view(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm()
    return render(request, 'cases/case_form.html', {'form': form})

@login_required

def case_update_view(request, pk):
    case = get_object_or_404(Case, pk=pk)
    if request.method == 'POST':
        form = CaseForm(request.POST, instance=case)
        if form.is_valid():
            form.save()
            return redirect('case_list')
    else:
        form = CaseForm(instance=case)
    return render(request, 'cases/case_form.html', {'form': form})


# cases/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Case, Hearing
from .forms import HearingForm

def hearing_create_view(request, case_number):
    case = get_object_or_404(Case, case_number=case_number)
    if request.method == 'POST':
        form = HearingForm(request.POST)
        if form.is_valid():
            hearing = form.save(commit=False)
            hearing.case = case
            hearing.save()
            return redirect('hearing_list', case_number=case_number)
    else:
        form = HearingForm(initial={'case': case})
    return render(request, 'cases/hearing_form.html', {'form': form, 'case': case})



def hearing_index(request):
    hearings = Hearing.objects.all()
    return render(request, 'cases/hearing_index.html', {'hearings': hearings})

def hearing_detail(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    return render(request, 'cases/hearing_detail.html', {'hearing': hearing})

def hearing_update(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    if request.method == 'POST':
        form = HearingForm(request.POST, instance=hearing)
        if form.is_valid():
            form.save()
            return redirect('hearing_detail', pk=hearing.pk)
    else:
        form = HearingForm(instance=hearing)
    return render(request, 'cases/hearing_form.html', {'form': form})
