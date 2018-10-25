from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
import json

from orders.models import Order


# Create your views here.
def order_deliver_status(request,order_id):
	try:
		status = Order.objects.all().filter(id=order_id).update(delivered=True)
		name = Order.objects.all().filter(id=order_id)[order_id-1].first_name
		response = json.dumps([{'Delivered': 'Order delivered to {} successfully'.format(name)}])
	except:
		response = json.dumps([{'Delivered': 'Wrong ID!'}])
	return HttpResponse(response,content_type='text/json')