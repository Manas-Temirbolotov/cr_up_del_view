from django.db import models


class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        app_label = 'item'

class Firma(models.Model):
    category_name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        app_label = 'item'

class Item(models.Model):
    name = models.CharField(max_length=20)
    price = models.FloatField()
    firma = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        app_label = 'item'
