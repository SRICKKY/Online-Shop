from django.urls import path
from .views import order_deliver_status

app_name = 'api'

urlpatterns = [
	path('deliver/<int:order_id>/',order_deliver_status,name='deliver_status')
]