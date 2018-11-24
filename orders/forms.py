from django import forms
from .models import Order

class OrderCreateForm(forms.ModelForm):
	address = forms.CharField(widget=forms.Textarea(attrs={'rows':5}))
	class Meta:
		model = Order
		fields = ['first_name','last_name','email','mobile','address','postal_code','city']

	def __init__(self,*args,**kwargs):
		super().__init__(*args,**kwargs)
		self.fields['first_name'].widget.attrs.update({'class':'form-control', 'placeholder': 'First Name'})
		self.fields['last_name'].widget.attrs.update({'class':'form-control','placeholder':'Last Name'})
		self.fields['email'].widget.attrs.update({'class':'form-control','placeholder':'Email'})
		self.fields['mobile'].widget.attrs.update({'class':'form-control','placeholder':'Mobile'})
		self.fields['address'].widget.attrs.update({'class':'form-control','placeholder':'Address'})
		self.fields['postal_code'].widget.attrs.update({'class':'form-control','placeholder':'PIN Code'})
		self.fields['city'].widget.attrs.update({'class':'form-control','placeholder':'Your City'})