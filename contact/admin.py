from django.contrib import admin
from contact.models import Contact


class ContactAdmin(admin.ModelAdmin):
    # Split the form into fieldsets.
    fieldsets = [
        # Tuple: ('title',{'fields':['field1', 'field2',]}
        (
            'Users contact info:', {
                'fields': [
                    'first_name', 
                    'last_name', 
                    'email', 
                    'company_name',
                    'has_been_contacted'
                ]
            }
        ),
        ('Prefers', {'fields': ['preferred_contact_method'], 'classes': ['collapse']}),
        ('Comments User has:', {'fields': ['comments'], 'classes': ['collapse']}),
    ]
    # Search for a specific contact via fields specified.
    search_fields = ['first_name', 'last_name', 'email']
    # What fields to list in Contacts admin view.
    list_display = (
        'first_name', 
        'last_name',
        'email', 
        'preferred_contact_method',
        'company_name',
        'last_modified',
        'has_been_contacted',
    )
    # Filter options to filter the Contacts admin view.
    list_filter = ['last_modified','has_been_contacted']
# Register your models here.
admin.site.register(Contact, ContactAdmin)
