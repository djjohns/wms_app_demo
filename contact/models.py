from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.contrib import admin
import datetime


class Contact(models.Model):
    PHONE = "phone"
    EMAIL = "email"
    PREFERRED_CONTACT_METHOD = [
        (PHONE, "Phone"),
        (EMAIL, "Email"),
    ]

    preferred_contact_method = models.CharField(
        max_length=5,
        choices=PREFERRED_CONTACT_METHOD,
        default=EMAIL,
    )
    company_name = models.CharField(
        # help_text="Company's name",
        max_length=200,
        validators=[MinLengthValidator(2, "Please enter your company's name.")],
    )
    first_name = models.CharField(
        # help_text="First name",
        max_length=200,
        validators=[MinLengthValidator(2, "Please enter your first name name.")],
    )
    last_name = models.CharField(
        # help_text="Last name",
        max_length=200,
        validators=[MinLengthValidator(2, "Please enter your last name name.")],
    )
    email = models.CharField(
        # help_text="E-mail",
        max_length=200,
        validators=[MinLengthValidator(2, "Please enter your E-mail address.")],
    )
    phone_number = models.CharField(
        # help_text="Phone number",
        max_length=12,
        validators=[MinLengthValidator(10, "Please enter your phone number.")],
    )
    comments = models.CharField(
        # help_text="Max 200 characters.",
        max_length=200,
        validators=[
            MinLengthValidator(0, "Let us know what service you are interested in.")
        ],
    )
    # owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    has_been_contacted = models.BooleanField(default=False)
    
    last_modified = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.company_name

    @admin.display(
        boolean=True,
        ordering='last_modified',
        description='Modified recently?',
    )
    def was_modified_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.last_modified <= now