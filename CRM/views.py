from django.shortcuts import render
from store.models import Order
from store.models import ShippingAddress
from store.models import OrderItem
# Create your views here.


def orders(request):
    order = Order.objects.all()
    item = OrderItem.objects.all()
    address = ShippingAddress.objects.all()
    context = {'order':order, 'address': address, 'item':item}
    return render(request, 'crm/orders.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    # item = OrderItem.objects.all()
    # address = ShippingAddress.objects.all()
    context = {'order':order}
    return render(request, 'crm/updateOrder.html')
