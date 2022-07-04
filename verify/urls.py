from django.urls import path, reverse_lazy
from . import views

app_name = "verify"
urlpatterns = [
    path(
        "verify/verify_product",
        views.VerifyProductView.as_view(
            success_url=reverse_lazy("verify:verify_product")
        ),
        name="verify_product",
    ),
    path(
        "verify/<int:pk>/update",
        views.VerifyUpdateView.as_view(
            success_url=reverse_lazy("verify:verify_update")
        ),
        name="verify_update",
    ),
    path(
        "verify/<int:pk>/delete",
        views.VerifyDeleteView.as_view(
            success_url=reverse_lazy("verify:verify_delete")
        ),
        name="verify_delete",
    ),
]
