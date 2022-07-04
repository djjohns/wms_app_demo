from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Inventory(models.Model):
    customer_number = models.CharField(
        max_length=10,
        validators=[
            MinLengthValidator(
                10,
            )
        ],
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(
        help_text="Measured in oz.", max_digits=6, decimal_places=2
    )
    upc = models.BigIntegerField(
        help_text="Please scan the UPC.",
    )
    qty = models.BigIntegerField(
        help_text="Please enter the quantity.",
    )
    warehouse = models.CharField(
        help_text="Please enter the warehouse.",
        max_length=2,
        validators=[MinLengthValidator(2, "Please enter the warehouse id.")],
    )
    location = models.CharField(
        help_text="Please enter the location sloted.",
        max_length=10,
        validators=[MinLengthValidator(10, "Please scan the location.")],
    )

    # Shows up in the admin list
    def __str__(self):
        return self.customer_number
