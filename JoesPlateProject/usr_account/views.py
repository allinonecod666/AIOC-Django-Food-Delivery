from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth import login, logout

def usr_reg_app(request):

    if request.method == 'POST':
        form_ucf = UserCreationForm(request.POST)
        if form_ucf.is_valid():
            username = form_ucf.cleaned_data.get('username')
            password = form_ucf.cleaned_data.get('password')
            gusr = authenticate(username=username, password=password)
            login(request, gusr)
            return redirect('/')
    else:
        form_ucf = UserCreationForm()
    context = {
        'form_ucf': form_ucf,
    }
    return render(request, 'usr_account/usr_register.html', context)

def usr_log_app(request):
    if request.method == 'POST':
        form_uaf = AuthenticationForm(data=request.POST)
        if form_uaf.is_valid():
            gusr = form_uaf.get_user()
            login(request, gusr)
            return redirect('/')
    else:
        form_uaf = AuthenticationForm()
    context = {
        'form_uaf': form_uaf,
    }
    return render(request, 'usr_account/usr_login.html', context)

def rest_reg_app(request):
    if request.method == 'POST':
        form_ucf = UserCreationForm(request.POST)
        if form_ucf.is_valid():
            gusr = form_ucf.save()
            login(request, gusr)
            return redirect('/')
    else:
        form_ucf = UserCreationForm()
    context = {
        'form_ucf': form_ucf,
    }
    return render(request, 'usr_account/rest_register.html', context)

def rest_log_app(request):
    if request.method == 'POST':
        form_uaf = AuthenticationForm(request.POST)
        if form_uaf.is_valid():
            login(request, form_uaf.get_user)
            return redirect('/')
    else:
        form_uaf = AuthenticationForm()
    context = {
        'form_ucf': form_uaf,
    }
    return render(request, 'usr_account/rest_login.html', context)
