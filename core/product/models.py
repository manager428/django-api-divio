from django.db import models
from core.abstract.models import AbstractModel


class Product(AbstractModel):
    title = models.TextField(blank=False, null=False)
    description = models.TextField(blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.name
