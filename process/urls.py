from django.urls import path, reverse_lazy
from . import views

app_name = "process"
urlpatterns = [
    path(
        "process/process_order",
        views.ProcessOrderView.as_view(
            success_url=reverse_lazy("process:process_order")
        ),
        name="process_order",
    ),
    path(
        "process/<int:pk>/update",
        views.ProcessUpdateView.as_view(
            success_url=reverse_lazy("process:process_update")
        ),
        name="process_update",
    ),
    path(
        "process/<int:pk>/delete",
        views.ProcessDeleteView.as_view(
            success_url=reverse_lazy("process:process_delete")
        ),
        name="process_delete",
    ),
]
