from django.contrib import admin

from main_app.models import Client


# admin.site.register(Client)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    search_fields = ('last_name', 'first_name')