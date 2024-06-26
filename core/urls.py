from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('', include('shop.urls'), name='index'),
    path('orders/', include('orders.urls', namespace='orders')),

]
