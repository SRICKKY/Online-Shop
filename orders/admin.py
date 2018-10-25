from django.contrib import admin
from .models import Order, OrderItem

# Register your models here.
class OrderItemInline(admin.TabularInline):
	model = OrderItem
	raw_id_fields = ['product']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
	list_display = ['id','first_name','last_name','email','mobile','address','postal_code','city','paid','delivered','created','updated']
	list_filter = ['paid','created','updated','delivered']
	# inlines = [OrderItemInline]

admin.site.register(OrderItem)