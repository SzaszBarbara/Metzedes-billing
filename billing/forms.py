from django import forms
from django.forms import TextInput, NumberInput, EmailInput

from billing.models import Product, Bill, Client, Car, ProductBill


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
        }


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
            'client': forms.Select(attrs={'class': 'form-select'}),
            'vin_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vin number'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter number plate'}),
            'engine_displacement': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter engine displacement'}),
            'colour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter colour'}),
        }

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter owner'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter code'}),
            'intern_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter internal code'}),
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the code'}),
            'intern_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the internal code'}),
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
            'workmanship': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of hours'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
        }

class BillUpdateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
            'workmanship': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of hours'}),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
        }


class ProductBillForm(forms.ModelForm):
    class Meta:
        model = ProductBill
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'internal_bill': forms.Select(attrs={'class': 'form-select'}),
            'purchasing_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchasing price'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter selling price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})
        }

class ProductBillUpdateForm(forms.ModelForm):
    class Meta:
        model = ProductBill
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'internal_bill': forms.Select(attrs={'class': 'form-select'}),
            'purchasing_price': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter purchasing price'}),
            'selling_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter selling price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})
        }