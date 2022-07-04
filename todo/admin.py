from django.contrib import admin
from todo.models import Task

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    # Split the form into fieldsets.
    fieldsets = [
        # Tuple: ('title',{'fields':['field1', 'field2',]}
        (
            'Task:', {
                'fields': [
                    'task_todo', 
                    'task_accomplished', 
                    'owner', 
                ]
            }
        ),
        ('Dependent on:', {'fields': ['task_dependencies'], 'classes': ['collapse']}),
    ]
    # Search for a specific contact via fields specified.
    search_fields = ['task_todo', 'owner']
    # What fields to list in Contacts admin view.
    list_display = (
        'task_todo', 
        'task_accomplished', 
        'owner', 
        'created_at',
        'updated_at'
    )
    # Filter options to filter the Contacts admin view.
    list_filter = ['owner','task_accomplished']

admin.site.register(Task, TaskAdmin)
