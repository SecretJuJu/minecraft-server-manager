from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import  AuthenticationForm


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('/')

    else:
        form = AuthenticationForm()

    context = {
        'form': form
    }

    return render(request, 'auth/login.html', context)
