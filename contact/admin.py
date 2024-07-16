from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactRegister(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email',
    ordering = '-id',
    list_per_page = 10
    list_max_show_all = 200

