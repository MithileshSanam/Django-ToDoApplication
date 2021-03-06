from django.db import models

# Create your models here.
class ToDoModel(models.Model):
    task = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.task
        
    class Meta:
        verbose_name_plural = "To Do Tasks"
