from django.contrib import admin
from django.contrib.admin import ModelAdmin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(ModelAdmin):
    list_display = ['name', 'is_done', 'date_add', 'date_update']
    list_filter = ['is_done', 'date_add', 'date_update']

