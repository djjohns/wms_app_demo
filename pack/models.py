from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings


class Pack(models.Model):
    order_number = models.CharField(
        help_text="Please scan the routing label.",
        max_length=10,
        validators=[MinLengthValidator(10, "Please scan the routing label.")],
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.order_number
