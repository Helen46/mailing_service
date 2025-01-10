from django.contrib import admin

from main_app.models import Client, MailingSetup, MailingMessage


# admin.site.register(Client)
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'last_name', 'first_name')
    search_fields = ('last_name', 'first_name')


@admin.register(MailingSetup)
class MailingSetupAdmin(admin.ModelAdmin):
    list_display = ('start', 'periodicity', 'status')
    search_fields = ('periodicity', 'status')


@admin.register(MailingMessage)
class MailingMessageAdmin(admin.ModelAdmin):
    list_display = ('topic',)
    search_fields = ('topic',)
