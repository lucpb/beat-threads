from django.db import models

class ShoppingCart(models.Model):

    def __str__(self):
        return self.name
    
class Wishlist(models.Model):

    def __str__(self):
        return self.name