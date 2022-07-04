from django.shortcuts import render
from contact.models import Contact
from django.core.mail import send_mail
from contact.no_owner import (
    NoOwnerCreateView,
    NoOwnerUpdateView,
    NoOwnerDeleteView,
)


def send_staff_email():
    # send an email notification
    send_mail(
        'first_name',  # Subject
        'comments',  # Message.
        'email',  # From Email.
        ['David.Johns@redtekindustries.com'],  # To Email.
        fail_silently=False,
    )
            

class ContactFormView(NoOwnerCreateView):
    model = Contact
    fields = [
        "company_name",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "comments",
        "preferred_contact_method",
    ]
    # send_staff_email()
    


class ContactUpdateView(NoOwnerUpdateView):
    model = Contact
    fields = [
        "company_name",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "comments",
        "preferred_contact_method",
    ]


class ContactDeleteView(NoOwnerDeleteView):
    model = Contact
