from django.contrib import auth, messages
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse

from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from shop.models import Basket

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


def profile (request):
    if request.method == 'POST':
        form = UserProfileForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
        else:
            print(form.errors)
    else:
        form = UserProfileForm(instance=request.user)

    baskets = Basket.objects.filter(user=request.user)
    total_sum = 0
    total_quantity = 0
    for basket in baskets:
        total_sum += basket.sum()
        total_quantity += basket.quantity

    context = {'form': form,
               'baskets': baskets,
               'total_sum': total_sum, 
               'total_quantity': total_quantity, 
            }
    return render (request, 'accounts/profile.html', context)