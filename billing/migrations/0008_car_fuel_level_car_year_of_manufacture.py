# Generated by Django 4.2.4 on 2023-09-13 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0007_bill_add_receipt_alter_bill_series'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='fuel_level',
            field=models.CharField(default='17%', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='car',
            name='year_of_manufacture',
            field=models.IntegerField(default=2013),
            preserve_default=False,
        ),
    ]
