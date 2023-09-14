import json
import os.path

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from billing.forms import ProductForm, BillForm, ClientForm, CarForm, ProductBillForm, ReceiptForm, \
    ProductBillUpdateForm
from billing.models import Client, Car, Product, Bill, ProductBill, Receipt


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, **kwargs):
        all_bills = Bill.objects.order_by('-id')
        return {
            'latest_bills': all_bills[0:min(3, len(all_bills))]
        }


class BillCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bill/create_bill.html'
    model = Bill
    form_class = BillForm

    def get_initial(self):
        return {'number': get_latest_number()}

    def get_success_url(self):
        save_latest_number(self.object.number + 1)
        return reverse_lazy('list-of-bills')


class BillListView(LoginRequiredMixin, ListView):
    template_name = 'bill/list_of_bills.html'
    model = Bill
    context_object_name = 'bills'


class BillUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'bill/update_bill.html'
    model = Bill
    form_class = BillForm
    success_url = reverse_lazy('list-of-bills')


class BillDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'bill/delete_bill.html'
    model = Bill
    success_url = reverse_lazy('list-of-bills')


class BillDetailView(LoginRequiredMixin, DetailView):
    template_name = 'bill/details_bill.html'
    model = Bill


class ProductBillCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product_bill/create_product_bill.html'
    model = ProductBill
    form_class = ProductBillForm
    success_url = reverse_lazy('list-of-product-bills')

    def get_initial(self):
        return self.request.GET


class ProductBillListView(LoginRequiredMixin, ListView):
    template_name = 'product_bill/list_of_product_bills.html'
    model = ProductBill
    context_object_name = 'productbills'


class ProductBillUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product_bill/update_product_bill.html'
    model = ProductBill
    form_class = ProductBillUpdateForm
    success_url = reverse_lazy('list-of-product-bills')


class ProductBillDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'product_bill/delete_product_bill.html'
    model = ProductBill
    success_url = reverse_lazy('list-of-product-bills')


class ProductBillDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product_bill/details_product_bill.html'
    model = ProductBill


class ProductCreateView(LoginRequiredMixin, CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-of-products')


class ProductListView(LoginRequiredMixin, ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'products'
    # permission_required = 'product.view_list_of_products'


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-of-products')


# class ProductDeleteView(DeleteView):
#     template_name = 'product/delete_product.html'
#     model = Product
#     success_url = reverse_lazy('list-of-products')


def delete_product(request, pk):
    Product.objects.filter(id=pk).delete()
    return redirect('list-of-products')


class ProductDetailView(LoginRequiredMixin, DetailView):
    template_name = 'product/details_product.html'
    model = Product


class ClientCreateView(LoginRequiredMixin, CreateView):
    template_name = 'client/create_client.html'
    model = Client
    form_class = ClientForm
    # context_object_name = 'clients'
    success_url = reverse_lazy('list-of-clients')


class ClientListView(LoginRequiredMixin, ListView):
    template_name = 'client/list_of_clients.html'
    model = Client
    context_object_name = 'all_clients'


# class ClientDeleteView(DeleteView):
#     template_name = 'client/delete_client.html'
#     model = Client
#     success_url = reverse_lazy('list-of-clients')


def delete_client(request, pk):
    Client.objects.filter(id=pk).delete()
    return redirect('list-of-clients')


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'client/update_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('list-of-clients')


class ClientDetailView(LoginRequiredMixin, DetailView):
    template_name = 'client/details_client.html'
    model = Client


class CarCreateView(LoginRequiredMixin, CreateView):
    template_name = 'car/create_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-of-cars')


class CarUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'car/update_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-of-cars')


class CarListView(LoginRequiredMixin, ListView):
    template_name = 'car/list_of_cars.html'
    # TODO This is what injects the model class into the template
    model = Car
    # TODO Add this to other views
    # This is going to be the name of the entity in the template
    context_object_name = 'cars'


class CarDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'car/delete_car.html'
    model = Car
    success_url = reverse_lazy('list-of-cars')


class CarDetailView(LoginRequiredMixin, DetailView):
    template_name = 'car/details_car.html'
    model = Car


class ReceiptCreateView(LoginRequiredMixin, CreateView):
    template_name = 'receipt/create_receipt.html'
    model = Receipt
    form_class = ReceiptForm
    success_url = reverse_lazy('list-of-bills')


class ReceiptUpdateView(LoginRequiredMixin, UpdateView):
    template_name = ''
    model = Car
    form_class = ReceiptForm
    success_url = reverse_lazy('list-of-bills')


class ReceiptListView(LoginRequiredMixin, ListView):
    template_name = ''
    model = Receipt
    context_object_name = 'receipts'


class ReceiptDeleteView(LoginRequiredMixin, DeleteView):
    template_name = ''
    model = Receipt
    success_url = reverse_lazy('list-of-bills')


class ReceiptDetailView(LoginRequiredMixin, DetailView):
    template_name = ''
    model = Receipt


class PrintCreateView(LoginRequiredMixin, CreateView):
    template_name = 'bill/print_bill.html'
    model = ''
    form_class = ''
    success_url = reverse_lazy('list-of-bills')


class PrintDetailView(LoginRequiredMixin, DetailView):
    model = Bill
    template_name = 'bill/print_bill.html'


class EstimateDetailsView(LoginRequiredMixin, DetailView):
    model = Bill
    template_name = 'estimate.html'


filename = 'latest_number.json'


def get_latest_number():
    if os.path.exists(filename):
        with open(filename) as file:
            number = json.load(file)
            return number
    else:
        first = 1
        save_latest_number(first)
    return first


def save_latest_number(number):
    with open(filename, 'wt') as file:
        json.dump(number, file)
