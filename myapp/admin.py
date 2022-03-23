from django.contrib import admin
from myapp.models import Contact

class ContactAdmin(admin.ModelAdmin):
    list = ('id', 'name', 'email', 'subject', 'message')
admin.site.register(Contact, ContactAdmin)