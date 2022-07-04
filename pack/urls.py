from django.urls import path, reverse_lazy
from . import views

app_name = "pack"
urlpatterns = [
    path(
        "pack/process_order",
        views.PackOrderView.as_view(success_url=reverse_lazy("pack:process_order")),
        name="process_order",
    ),
    path(
        "pack/<int:pk>/update",
        views.PackUpdateView.as_view(success_url=reverse_lazy("pack:pack_update")),
        name="pack_update",
    ),
    path(
        "pack/<int:pk>/delete",
        views.PackDeleteView.as_view(success_url=reverse_lazy("pack:pack_delete")),
        name="pack_delete",
    ),
]
