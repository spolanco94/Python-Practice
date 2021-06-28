from django.db import models
from django.db.models.base import Model

class Pizza(models.Model):
    """A pizza that the user is building."""
    name = models.CharField(max_length=150)

    def __str__(self) -> str:
        """Return the Pizza model name."""
        return self.name

class Topping(models.Model):
    """Toppings to be added to pizza."""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta: 
        verbose_name_plural = "toppings"

    def __str__(self) -> str:
        return f"{self.name}"