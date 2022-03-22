from django.contrib import admin
from myapp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list = ('name', 'email', 'subject', 'message')
admin.site.register(Contact, ContactAdmin)