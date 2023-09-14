from django import forms
from django.forms import TextInput, NumberInput, EmailInput, DateInput

from billing.models import Product, Bill, Client, Car, ProductBill, Receipt


class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'cif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cif'}),
            'reg_com': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter reg com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
        }


class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'name@example.com'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'cif': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter cif'}),
            'reg_com': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter reg com'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter address'}),
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
            'year_of_manufacture': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter year of manufacture'}),
            'fuel_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter fuel level'}),
        }

class CarUpdateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {
            'brand': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter brand'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter model'}),
            'client': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter owner'}),
            'vin_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vin number'}),
            'number_plate': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter number plate'}),
            'engine_displacement': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter engine displacement'}),
            'colour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter colour'}),
            'year_of_manufacture': forms.NumberInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter year of manufacture'}),
            'fuel_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter fuel level'}),
        }


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter code'}),
            'intern_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter internal code'}),
            'purchasing_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchasing price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})
        }


class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter name'}),
            'code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the code'}),
            'intern_code': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter the internal code'}),
            'purchasing_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchasing price'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter quantity'})
        }

class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
            'workmanship': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter amount'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'date_emitted': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bill number'}),
            'series': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter series'}),
            'estimate_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter estimate number'}),
            'repairing_start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'repairing_end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

class BillUpdateForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
            'workmanship': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter number of hours'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Please enter your description', 'rows': 3}),
            'date_emitted': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter bill number'}),
            'series': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter series'}),
            'estimate_number': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter estimate number'}),
            'repairing_start_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'repairing_end_date': DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }


class ProductBillForm(forms.ModelForm):
    class Meta:
        model = ProductBill
        fields = '__all__'
        widgets = {
            'product': forms.Select(attrs={'class': 'form-select'}),
            'internal_bill': forms.Select(attrs={'class': 'form-select'}),
            # 'purchasing_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter purchasing price'}),
            'percent_added': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter markup percentage'}),
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

class ReceiptForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
        }

class ReceiptUpdateForm(forms.ModelForm):
    class Meta:
        model = Receipt
        fields = '__all__'
        widgets = {
            'car': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Choose car'}),
        }