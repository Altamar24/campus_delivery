from django.urls import path
from django.contrib.auth.decorators import login_required

from accounts.views import UserLoginView, logout, UserProfileView, UserRegistrationView

app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('registration/', UserRegistrationView.as_view(), name='registration'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', login_required(UserProfileView.as_view()), name='profile'),
    
]