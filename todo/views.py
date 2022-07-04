from todo.models import Task
from todo.owner import (
    OwnerListView,
    OwnerDetailView,
    OwnerCreateView,
    OwnerUpdateView,
    OwnerDeleteView,
)

class TaskListView(OwnerListView):
    model = Task
    # By convention:
    template_name = "todo/task_list.html"


class TaskDetailView(OwnerDetailView):
    model = Task

class TaskTodoView(OwnerCreateView):
    model = Task
    fields = ["task_todo", "task_dependencies", "task_accomplished"]


class TaskUpdateView(OwnerUpdateView):
    model = Task
    fields = ["task_todo", "task_dependencies", "task_accomplished"]


class TaskDeleteView(OwnerDeleteView):
    model = Task
