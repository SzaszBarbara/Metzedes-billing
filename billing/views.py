from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from billing.forms import ProductForm, BillForm, ClientForm, CarForm, ProductBillForm
from billing.models import Client, Car, Product, Bill, ProductBill


class HomeTemplateView(TemplateView):
    template_name = 'home/homepage.html'


class BillCreateView(CreateView):
    template_name = 'bill/create_bill.html'
    model = Bill
    form_class = BillForm
    success_url = reverse_lazy('list-of-bills')


class BillListView(ListView):
    template_name = 'bill/list_of_bills.html'
    model = Bill
    context_object_name = 'bills'


class BillUpdateView(UpdateView):
    template_name = 'bill/update_bill.html'
    model = Bill
    form_class = BillForm
    success_url = reverse_lazy('list-of-bills')


class BillDeleteView(DeleteView):
    template_name = 'bill/delete_bill.html'
    model = Bill
    success_url = reverse_lazy('list-of-bills')


class BillDetailView(DetailView):
    template_name = 'bill/details_bill.html'
    model = Bill

class ProductBillCreateView(CreateView):
    template_name = 'product_bill/create_product_bill.html'
    model = ProductBill
    form_class = ProductBillForm
    success_url = reverse_lazy('list-of-product-bills')


class ProductBillListView(ListView):
    template_name = 'product_bill/list_of_product_bills.html'
    model = ProductBill
    context_object_name = 'productbills'


class ProductBillUpdateView(UpdateView):
    template_name = 'product_bill/update_product_bill.html'
    model = ProductBill
    form_class = ProductBillForm
    success_url = reverse_lazy('list-of-product-bills')


class ProductBillDeleteView(DeleteView):
    template_name = 'product_bill/delete_product_bill.html'
    model = ProductBill
    success_url = reverse_lazy('list-of-product-bills')


class ProductBillDetailView(DetailView):
    template_name = 'product_bill/details_product_bill.html'
    model = ProductBill



class ProductCreateView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list-of-products')


class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'products'
    # permission_required = 'product.view_list_of_products'


class ProductUpdateView(UpdateView):
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


class ProductDetailView(DetailView):
    template_name = 'product/details_product.html'
    model = Product


class ClientCreateView(CreateView):
    template_name = 'client/create_client.html'
    model = Client
    form_class = ClientForm
    # context_object_name = 'clients'
    success_url = reverse_lazy('list-of-clients')


class ClientListView(ListView):
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


class ClientUpdateView(UpdateView):
    template_name = 'client/update_client.html'
    model = Client
    form_class = ClientForm
    success_url = reverse_lazy('list-of-clients')


class ClientDetailView(DetailView):
    template_name = 'client/details_client.html'
    model = Client


class CarCreateView(CreateView):
    template_name = 'car/create_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-of-cars')


class CarUpdateView(UpdateView):
    template_name = 'car/update_car.html'
    model = Car
    form_class = CarForm
    success_url = reverse_lazy('list-of-cars')


class CarListView(ListView):
    template_name = 'car/list_of_cars.html'
    # TODO This is what injects the model class into the template
    model = Car
    # TODO Add this to other views
    # This is going to be the name of the entity in the template
    context_object_name = 'cars'



class CarDeleteView(DeleteView):
    template_name = 'car/delete_car.html'
    model = Car
    success_url = reverse_lazy('list-of-cars')


class CarDetailView(DetailView):
    template_name = 'car/details_car.html'
    model = Car
