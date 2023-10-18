from django.db import models

# Create your models here.

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PetroleumProduct(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Sale(models.Model):
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    product = models.ForeignKey(PetroleumProduct, on_delete=models.CASCADE)
    year = models.IntegerField()
    sales = models.DecimalField(max_digits=10, decimal_places=2)



