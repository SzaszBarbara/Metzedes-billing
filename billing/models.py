from django.contrib.auth.models import AbstractUser
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    cif = models.CharField(max_length=50)
    reg_com = models.CharField(max_length=50)
    address = models.CharField(max_length=255)

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
    year_of_manufacture = models.IntegerField()
    fuel_level = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f'{self.client} - {self.brand} {self.model}' \
               f''


class Product(models.Model):
    name = models.CharField(max_length=255)
    code = models.IntegerField()
    intern_code = models.IntegerField()
    purchasing_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f'{self.name} - code: {self.code}, intern code: {self.intern_code}'


class Bill(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    workmanship = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.TextField(null=True, blank=True)
    date_emitted = models.DateField(null=True, blank=True)
    number = models.IntegerField()
    series = models.CharField(max_length=10, default='ODC')
    estimate_number = models.IntegerField()
    repairing_start_date = models.DateField(null=True, blank=True)
    repairing_end_date = models.DateField(null=True, blank=True)
    add_receipt = models.BooleanField(default=False)


    def __str__(self):
        return f'#{self.id} for {self.car}'

    def selling_total(self):
        product_bills = self.productbill_set.all()
        total = 0
        for product_bill in product_bills:
            total += product_bill.selling_total()
        return total

    def products_count(self):
        return sum([p.quantity for p in self.productbill_set.all()])

    def total_estimate(self):
        return self.selling_total() + self.workmanship
        # return self.selling_total() + float(self.workmanship)

class ProductBill(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    internal_bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
    percent_added = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField(default=1)

    def selling_price(self):
        return self.product.purchasing_price + self.product.purchasing_price * self.percent_added

    def selling_total(self):
        return self.selling_price() * self.quantity

    def __str__(self):
        return f'{self.quantity} {self.product}, factura: {self.internal_bill} ' \
               f'pret: {self.product.purchasing_price} lei, adaos: {self.percent_added}%'


# chitanta
class Receipt(models.Model):
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)

    # def __str__(self):
    #     return f'{self.product.name}'

# file = models.FileField(upload_to='billing_files/')
