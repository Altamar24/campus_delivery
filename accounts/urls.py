from django.urls import path

from accounts.views import login, registration

app_name = 'accounts'

urlpatterns = [
    path('login/', login, name='login'),
    path('registration/', registration, name='registration'),
]