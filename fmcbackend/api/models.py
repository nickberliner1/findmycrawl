from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from decimal import Decimal

# Create your models here.

class Event(models.Model):
    name = models.CharField(max_length=60)
    main_picture = models.FileField(blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=6, decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))], blank=True, null=True)
    comes_with_free_drinks = models.BooleanField(blank=True, null=True)
    # This is giving me trouble
    # date = models.DateField(default = date.today)
    start_time = models.TimeField(blank=True, null=True)

    # objects = QuerySetManager()

    def __str__(self):
        return self.name