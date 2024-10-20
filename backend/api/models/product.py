from django.db import models

class Product(models.Model):

    def __str__(self):
        return self.name
    
class Category(models.Model):

    def __str__(self):
        return self.name
    
class Inventory(models.Model):

    def __str__(self):
        return self.name
    
class ProductReview(models.Model):

    def __str__(self):
        return self.name