from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
	'''
	Task to send an e-mail notification when an order is successfully created.
	'''

	order = Order.objects.get(id=order_id)
	subject = 'Order number {}'.format(order.id)
	message = '''
	Dear {},
	You have successfully placed an order.
	Your Order ID is {}
	'''.format(order.first_name,order.id)

	mail_sent = send_mail(subject,message,'admin@myshop.com',[order.email])




	return mail_sent

@task
def mail_logistic(order_id):
	'''
	Task to send an e-mail notification to Logistic Management
	'''
	order = Order.objects.get(id=order_id)
	subject = 'Oder number {}'.format(order.id)
	message = '''
	A new order has been placed by {}.
	Contact Number: {}
	The delivery address is 
	{}
	{}
	'''.format(order.first_name,order.mobile,order.address,order.city,order.postal_code)

	mail_sent = send_mail(subject,message,'admin@myshop.com',['logistic@gmail.com'])

	return mail_sent
	# Stocking Out Product
	# Product.objects.filter(name='Black Tea').update(stock=20)