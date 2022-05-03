from tkinter import CASCADE
from django.db import models


# Create your models here.
# todo ~list model outline-
# name prop char field max 100
# created_on property with date and time,
# should default to that using auto_now_add feature
# a __str__ method that returns the value of the
# todolists -name- property

class TodoList(models.Model):
    name = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


# todo ~item
# task prop char up max value 100
# due_date prop contains an optional date and time of item comp
# is_complete property that indicates TRUE is completed OR
# false is NOT
# a list prop that is foreign key relationship to todolist
# that creates a collection named items, and will auto delete
# items if the to do list is deleted- CASCADE
# a str method that returns the value of todoitems task prop

class TodoItem(models.Model):
    task = models.CharField(max_length=100)
    due_date = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    list = models.ForeignKey(
        "Todolist", related_name="items", on_delete=models.CASCADE,)

    def __str__(self):
        return str(self.task)
