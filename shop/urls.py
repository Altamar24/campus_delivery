from django.urls import path

from .views import product_list, product_detail, index, basket_add, basket_delete

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('product_list/', product_list, name='product_list'),
    path('<slug:category_slug>/', product_list, name='product_list_by_category'),
    path('<int:id>/<slug:slug>/', product_detail, name='product_detail'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', basket_delete, name='basket_delete'),
]
