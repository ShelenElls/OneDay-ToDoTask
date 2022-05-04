from django.urls import path, include

from todos.views import (
    TodoCreateView,
    TodoListView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
    TodoItemCreateView,
    TodoItemUpdateView,
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_details"), 
    path("create", TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete"),
    path("<int:pk>/edit", TodoUpdateView.as_view(), name="todo_edit"),
    path("items/create/", TodoItemCreateView.as_view(), name="todo_item_create"),
    path("items/<int:pk>/edit/", TodoItemUpdateView.as_view(),name="todo_item_update"),
]