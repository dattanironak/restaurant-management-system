from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from menu.models import Menu


class Bill(models.Model) :
    table_no = models.IntegerField(null=False)
    bill_date = models.DateTimeField(null=False)
    is_active = models.BooleanField(default=True)
    total = models.IntegerField(null=False, default=0)
    discount = models.IntegerField(default=0)
    is_printed = models.BooleanField(default=False)


class BillMenu(models.Model):
    bill_id = models.ForeignKey(Bill, on_delete=models.CASCADE)
    item_id = models.ForeignKey(Menu, on_delete=models.RESTRICT)
    item_name = models.CharField(max_length=100)
    item_price = models.IntegerField(default=0)
    quantity = models.SmallIntegerField(default=0)
    item_total = models.IntegerField(default=0)