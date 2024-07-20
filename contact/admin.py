from django.contrib import admin
from contact import models

@admin.register(models.Contact)
class ContactRegister(admin.ModelAdmin):
    list_display = 'id', 'first_name', 'last_name', 'email', 'category', 'show'
    ordering = '-id',
    list_per_page = 10
    list_max_show_all = 200
    list_editable = 'show',

@admin.register(models.Category)
class CategoryRegister(admin.ModelAdmin):
    list_display = 'name',
    ordering = '-id',



