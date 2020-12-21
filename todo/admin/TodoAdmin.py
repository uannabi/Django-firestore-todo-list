from django.contrib import admin


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created')
    search_fields = ('title',)
