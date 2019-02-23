from django.shortcuts import render

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import OrderItem
from .tasks import mail_logistic, order_created


# Create your views here.
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity'])
                # Clear the cart
                cart.clear()
                order_created.delay(order.id)
                mail_logistic.delay(order.id)
                return render(request, 'orders/order/created.html', {'order': order})
    else:
        form = OrderCreateForm()

    return render(request, 'orders/order/create.html',
                  {'cart': cart, 'form': form})
