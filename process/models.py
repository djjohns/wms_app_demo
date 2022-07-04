from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Process(models.Model):
    order_number = models.CharField(
        help_text="Please scan the tray id.",
        max_length=10,
        validators=[MinLengthValidator(10, "Please scan the tray id.")],
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    weight = models.DecimalField(
        help_text="Measured in oz.", max_digits=6, decimal_places=2
    )
    upc = models.BigIntegerField(
        help_text="Please scan the UPC.",
    )

    # Shows up in the admin list
    def __str__(self):
        return self.order_number
