from django.db import models
from django.urls import reverse # new

# Create your models here.
class Shop(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('s_detail', args=[str(self.id)])

class Product(models.Model):
    name = models.CharField(max_length=200)
    exp_date = models.DateField()
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('p_detail', args=[str(self.id)])

class Staff(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=200)
    shop = models.ForeignKey(
        Shop,
        on_delete=models.CASCADE,
    )
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('st_detail', args=[str(self.id)])

