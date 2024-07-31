from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Case, Hearing
from .forms import LoginForm, CustomUserCreationForm, CaseForm, HearingForm

# General Views
def frontpage_view(request):
    return render(request, 'cases/index.html')

def about_view(request):
    return render(request, 'cases/about.html')

def contact_view(request):
    return render(request, 'cases/contact.html')

# Authentication Views
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.username == 'court':
                return redirect('case_list')
            elif user.username == 'judge':
                return redirect('case_list_judge')
            else:
                return redirect('case_add_hearing')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html')



def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('login')
        else:
            messages.error(request, 'Registration failed. Please correct the errors.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

# Case Views
@login_required
def case_list_view(request):
    if request.user.username == 'judge':
        cases = Case.objects.all()
        return render(request, 'cases/case_list.html', {'cases': cases, 'read_only': True})
    elif request.user.username != 'court':
        messages.error(request, 'You do not have permission to access this page.')
        return render(request, 'cases/index.html')
    cases = Case.objects.all()
    return render(request, 'cases/case_list.html', {'cases': cases})



@login_required
def case_detail_view(request, case_number):
    case = get_object_or_404(Case, case_number=case_number)
    return render(request, 'cases/case_detail.html', {'case': case})

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
def case_add_hearing_view(request):
    if request.method == 'POST':
        form = CaseForm(request.POST)
        if form.is_valid():
            case = form.save()
            messages.success(request, 'Case added successfully.')
            return redirect('hearing_create', case_number=case.case_number)
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

# Hearing Views
@login_required
def hearing_list_view(request, case_number):
    case = get_object_or_404(Case, case_number=case_number)
    hearings = case.hearings.all()
    if request.user.username == 'judge':
        return render(request, 'cases/hearing_list.html', {'case': case, 'hearings': hearings, 'read_only': True})
    return render(request, 'cases/hearing_list.html', {'case': case, 'hearings': hearings})



@login_required
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

@login_required
def hearing_index_view(request):
    hearings = Hearing.objects.all()
    return render(request, 'cases/hearing_index.html', {'hearings': hearings})

@login_required
def hearing_detail_view(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    return render(request, 'cases/hearing_detail.html', {'hearing': hearing})

@login_required
def hearing_update_view(request, pk):
    hearing = get_object_or_404(Hearing, pk=pk)
    case_number = hearing.case.case_number  # Get the case number related to the hearing
    if request.method == 'POST':
        form = HearingForm(request.POST, instance=hearing)
        if form.is_valid():
            form.save()
            return redirect('hearing_list', case_number=case_number)  # Redirect to the hearing list after saving
    else:
        form = HearingForm(instance=hearing)
    return render(request, 'cases/hearing_form.html', {'form': form, 'case': hearing.case})



@login_required
def case_list_judge_view(request):
    if request.user.username != 'judge':
        messages.error(request, 'You do not have permission to access this page.')
        return redirect('frontpage')
    cases = Case.objects.all()
    return render(request, 'cases/case_list.html', {'cases': cases, 'read_only': True})

