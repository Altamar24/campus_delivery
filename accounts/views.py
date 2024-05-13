from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.contrib.auth.views import LoginView
from django.http.response import HttpResponse as HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from accounts.models import User, EmailVerification
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


class EmailVerificationView(TemplateView):
    template_name = 'accounts/email_verification.html'

    def get(self, request, *args, **kwargs):
        code = kwargs['code']
        user = User.objects.get(email=kwargs['email'])
        email_verifications = EmailVerification.objects.filter(user=user, code=code)
        if email_verifications.exists() and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super(EmailVerificationView, self).get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('shop:index'))

