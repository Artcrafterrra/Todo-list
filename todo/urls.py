from django.urls import path
from todo.views import (
    TaskListView,
    toggle_task,
    TaskDeleteView,
    TaskUpdateView,
    TaskCreateView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)


app_name = "todo"

urlpatterns = [
    path("", TaskListView.as_view(), name="task-list"),
    path("<int:pk>/toggle/", toggle_task, name="task-toggle"),
    path("<int:pk>/delete/", TaskDeleteView.as_view(), name="task-delete"),
    path("<int:pk>/update/", TaskUpdateView.as_view(), name="task-update"),
    path("create/", TaskCreateView.as_view(), name="task-create"),
    path("tags/", TagListView.as_view(), name="tag-list"),
    path("tags/create/", TagCreateView.as_view(), name="tag-create"),
    path("tags/<int:pk>/update/", TagUpdateView.as_view(), name="tag-update"),
    path("tags/<int:pk>/delete/", TagDeleteView.as_view(), name="tag-delete"),
]
