from django.contrib import admin
from .models import TodoCategory, Task


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class TaskAdmin(admin.ModelAdmin):
    exclude = ('date_created',)


admin.site.register(TodoCategory, CategoryAdmin)
admin.site.register(Task, TaskAdmin)
