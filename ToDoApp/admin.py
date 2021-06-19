from django.contrib import admin

# Register your models here.
from ToDoApp.models import ToDoModel

admin.site.register(ToDoModel)
