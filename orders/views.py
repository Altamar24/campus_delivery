from django.forms import BaseModelForm
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderForm

class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreateView, self).form_valid(form)
