from django.contrib import admin

from billing.models import Client, Product, Car, ProductBill, Bill

admin.site.register(Client)
admin.site.register(Car)
admin.site.register(Product)
admin.site.register(Bill)
admin.site.register(ProductBill)
# admin.site.register(Receipt)
