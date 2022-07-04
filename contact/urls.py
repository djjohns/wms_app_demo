from django.urls import path, reverse_lazy
from . import views

app_name = "contact"
urlpatterns = [
    path(
        "contact/contact_form",
        views.ContactFormView.as_view(success_url=reverse_lazy("contact:contact_form")),
        name="contact_form",
    ),
    path(
        "contact/<int:pk>/update",
        views.ContactUpdateView.as_view(
            success_url=reverse_lazy("contact:contact_update")
        ),
        name="contact_update",
    ),
    path(
        "contact/<int:pk>/delete",
        views.ContactDeleteView.as_view(
            success_url=reverse_lazy("contact:contact_delete")
        ),
        name="contact_delete",
    ),
]
