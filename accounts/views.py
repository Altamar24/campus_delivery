from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import CreateView, UpdateView

from accounts.models import User
from accounts.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from shop.models import Basket

class UserLoginView(LoginView):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('')


class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'accounts/registration.html'
    success_url = reverse_lazy('accounts:login')


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'accounts/profile.html'

    def get_success_url(self):
        return reverse_lazy('accounts:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data()
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop:index'))

