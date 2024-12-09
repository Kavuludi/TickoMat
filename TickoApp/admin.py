from django.contrib import admin

from TickoApp.models import Client, Admin, Contact, Booking

# Register your models here.
admin.site.register(Client)
admin.site.register(Admin)
admin.site.register(Contact)
admin.site.register(Booking)

