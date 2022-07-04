from django.urls import path, reverse_lazy
from . import views

app_name = "todo"
urlpatterns = [
    # path("todo", views.TaskListView.as_view()),
    path("todo/all", views.TaskListView.as_view(),name='all'),
    path("todo/<int:pk>", views.TaskDetailView.as_view(), name="task_detail"),
    path(
        "todo/task",
        views.TaskTodoView.as_view(success_url=reverse_lazy("todo:task_form")),
        name="task_form",
    ),
    path(
        "todo/<int:pk>/update",
        views.TaskUpdateView.as_view(success_url=reverse_lazy("todo:task_update")),
        name="task_update",
    ),
    path(
        "todo/<int:pk>/delete",
        views.TaskDeleteView.as_view(success_url=reverse_lazy("todo:task_delete")),
        name="task_delete",
    ),
    
]
