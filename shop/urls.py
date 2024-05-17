from django.urls import path

from .views import ProductsListView, IndexView, basket_add, basket_delete

app_name = 'shop'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('product_list/', ProductsListView.as_view(), name='product_list'),
    path('category/<int:category_id>/', ProductsListView.as_view(), name='category'),
    path('page/<int:page>/', ProductsListView.as_view(), name='paginator'),
    path('<slug:category_slug>/', ProductsListView.as_view(), name='product_list_by_category'),
    path('basket/add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket/delete/<int:basket_id>/', basket_delete, name='basket_delete'),
]
