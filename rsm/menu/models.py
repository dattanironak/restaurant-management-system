from django.db import models


# Create your models here.
class Menu(models.Model):
    categories = ['Punjabi', 'Kathiyawadi', 'Chinese', 'Maxican', 'Fastfood', 'Beverages', 'Dessert', 'Bread', 'Starter']
    item_name = models.CharField(max_length=40, unique=True)
    item_id = models.CharField(primary_key=True, max_length=3)
    category = models.CharField(choices=((c,c) for c in categories), max_length=15, null=False)
    price = models.IntegerField(null=False)
    is_available = models.BooleanField(default=True)