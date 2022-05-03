from msilib.schema import ListView
from pyexpat import model
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from todos.models import TodoItem, TodoList



# Create your views here.
# LIST VIEW
# path config- /todos/ 
# either function view or class view
# when a request is made to the path, must have 
# 200 status code- html in browser must have- 
# each todo lists name in it
# link to detail page of EACH todo list
# link to create page for todo list
# link to create page for todo item
# class ModelNameListView(ListView):
    # model = ModelName
    # template_name = "model_names/list.html"

class TodoListView(ListView):
    model = TodoList
    template_name = "todolist.html"
    # context_object_name = "todo_list"

    def __str__(self):
        return str(self.name)

# # DETAIL list VIEW
# path config /todos/<int:pk>/
# link to the delete page for the todo list
# link to the edit page for the todo list
# each todo item in the todo list, a link to that todo items
# edit page. 
# class ModelNameDetailView(DetailView):
#     model = ModelName
#     template_name = "model_names/detail.html"
class TodoDetailView(DetailView):
    model = TodoList
    template_name = "tododetail.html"
    
    def __str__(self):
        return str(self.name)    


# CREATE list VIEW
# path config /todo/create
# html must have- a form with the mthod -'post'
# an input with the name- 'name'
# when the form is submitted with a non-empty value for
# 'name- redirect to another page. 
#creates todolist record in database 
# when form is submitted with empty value for name-
# form is not valid, and page does NOT redirect. 
# class ModelNameCreateView(CreateView):
#     model = ModelName
#     template_name = "model_names/create.html"
#     fields = ["model", "properties", "for", "your", "form"]

#     # Redirects to the detail page for the
#     # instance just created, assuming that
#     # the path name is registered
#     def get_success_url(self):
#         return reverse_lazy("model_name_detail", args=[self.object.id])

class TodoCreateView(CreateView):
    model = TodoList
    template_name = "todo/create.html"
    fields = ["Task", "Due date", "Is completed", "List", ]
    
    def get_success_url(self):
        return reverse_lazy("todo_details", args=[self.object.id])
    
    def __str__(self):
        return str(self.name)    


# UPDATE list VIEW
# path- /todo/<int:pk>/edit/
# a form with the mothod- post
# an input with the name- name 
# the input must have the name of the todo list
# as its value (must see it in text box)
# form is submitted with non-empty value for name- 
# same process as create view- no redirect for invalid form
# class ModelNameUpdateView(UpdateView):
#     model = ModelName
#     template_name = "model_names/update.html"
#     fields = ["model", "properties", "for", "your", "form"]

#     # Redirects to the detail page for the
#     # instance just created, assuming that
#     # the path name is registered
#     def get_success_url(self):
#         return reverse_lazy("model_name_detail", args=[self.object.id])
class TodoUpdateView(UpdateView):
    model = TodoList
    template_name = "todo/update.html"
    fields = ["Task", "Due date", "Is completed", "List", ]

    def get_success_url(self):
        return reverse_lazy("todo_details", args=[self.object.id])

    def __str__(self):
        return str(self.name)   

# DELETE list VIEW
# path /todos/<int:pk>/delete/
# a form with the method post
# when submitted- redirects to another page,
# removes todo from database/removes all associated
# class ModelNameDeleteView(DeleteView):
#     model = ModelName
#     template_name = "model_names/delete.html"

#     # Redirects to the list view for the model
#     # assuming that the path name is registered
#     success_url = reverse_lazy("model_name_list")
class TodoDeleteView(DeleteView):
    model = TodoList
    template_name = "todo/delete.html"

    success_url = reverse_lazy("todo_list")

class TodoItemCreateView(CreateView):
    model = TodoItem
    template_name = "todo/items/create.html"