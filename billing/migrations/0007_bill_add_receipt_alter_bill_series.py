# Generated by Django 4.2.4 on 2023-09-12 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billing', '0006_bill_date_emitted_bill_number_bill_series_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='add_receipt',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='bill',
            name='series',
            field=models.CharField(default='ODC', max_length=10),
        ),
    ]