from django.contrib import admin
from todo.models import Category,Todo
from todo.admin.TodoAdmin import TodoAdmin

admin.site.register(Category)
admin.site.register(Todo,TodoAdmin)