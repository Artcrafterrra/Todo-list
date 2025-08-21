from django.contrib import admin

from todo.models import Task, Tag


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ("content", "is_done", "created", "deadline")
    list_filter = ("is_done", "created", "tags")
    search_fields = ("content",)
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
