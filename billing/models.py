from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    brand = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    vin_number = models.CharField(max_length=255)
    number_plate = models.CharField(max_length=255)
    engine_displacement = models.IntegerField()
    colour = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.client} - {self.brand} {self.model}' \
               f''


class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    intern_code = models.IntegerField()

    # purchasing_price = models.DecimalField(max_digits=10, decimal_places=2)
    # quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - code: {self.code}, intern code: {self.intern_code}'


class Bill(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workmanship = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'Bill {self.id} for {self.car}'

    def total(self):
        product_bills = self.productbill_set.all()
        total = 0
        for product_bill in product_bills:
            total += product_bill.selling_price()
        return total

    def products_count(self):
        return sum([p.quantity for p in self.productbill_set.all()])
class ProductBill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    internal_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    purchasing_price = models.DecimalField(max_digits=10, decimal_places=2)
    percent_added = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def selling_price(self):
        return self.purchasing_price + self.purchasing_price * self.percent_added

    def __str__(self):
        return f'{self.quantity} buc. din {self.product} de pe factura {self.internal_bill} ' \
               f'are ca pret: {self.purchasing_price} lei si adaos {self.percent_added}'


# chitanta
class Receipt(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.product.name}'

# file = models.FileField(upload_to='billing_files/')
