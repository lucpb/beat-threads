from django.db import models

class Discount(models.Model):

    def __str__(self):
        return self.name