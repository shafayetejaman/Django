from django.db import models
from category.models import Category

# Create your models here.
class Task(models.Model):
    task_title = models.CharField(max_length=50)
    task_description = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    date_assigned = models.DateField()
    category = models.ManyToManyField(Category)