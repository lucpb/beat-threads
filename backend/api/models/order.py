from django.db import models

class Order(models.Model):

    def __str__(self):
        return self.name
    
class OrderItem(models.Model):

    def __str__(self):
        return self.name
    
class Payment(models.Model):

    def __str__(self):
        return self.name
    
class ShippingAddress(models.Model):

    def __str__(self):
        return self.name