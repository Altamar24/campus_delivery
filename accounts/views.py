from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from accounts.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        form = UserLoginForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегестрированы!')
            return HttpResponseRedirect(reverse('accounts:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'accounts/registration.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop:index'))