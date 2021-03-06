# Generated by Django 3.1.5 on 2021-02-13 11:46

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_event_ticket_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ticket_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]
