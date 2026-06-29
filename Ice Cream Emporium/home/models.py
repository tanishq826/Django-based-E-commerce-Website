from django.db import models


# makemigrations- create changes and store it in a file
# migrate- apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name=models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Products(models.Model):
    img=models.CharField(max_length=512, null=True, blank=True)
    name = models.CharField(max_length=122)
    price = models.IntegerField(max_length=10)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")

    def __str__(self):
        return f"{self.name},{self.price},{self.category.name}"
        
   

class Cart(models.Model):
    img=models.CharField(max_length=512, null=True, blank=True)
    products=models.ForeignKey(Products,on_delete=models.CASCADE)
    quantity=models.IntegerField(max_length=10)
    price=models.IntegerField(max_length=122)


    def __str__(self):
        return f"{self.product.name} ({self.quantity})"

