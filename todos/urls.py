from django.urls import path, include

from todos.views import (
    TodoCreateView,
    TodoListView,
    TodoDetailView,
    TodoUpdateView,
    TodoDeleteView,
    
)

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("<int:pk>/", TodoDetailView.as_view(), name="todo_details"), 
    path("<int:pk>/create", TodoCreateView.as_view(), name="todo_create"),
    path("<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete"),
    path("<int:pk>/edit", TodoUpdateView.as_view(), name="todo_edit"),

]