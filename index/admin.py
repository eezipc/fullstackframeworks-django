
from django.contrib import admin
from .models import Contact
# Add fields to admin page on website.


class AdminContactForm(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'message',
    )


admin.site.register(Contact, AdminContactForm)
