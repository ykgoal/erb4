from django.contrib import admin

from .models import Contact
# Register your models here.

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'listing_id', 'email', 'phone', 'message', 'contact_date', 'user_id', )


    list_display_links = ('id', 'name', )
    search_fields = ('name', 'email', 'listing', )
    list_per_page = 25

    '''
    list_filter = 'realtor',
    list_editable = 'is_published',

    '''

admin.site.register(Contact, ContactsAdmin)