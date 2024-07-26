from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_by = models.CharField(max_length=50)
    created_time = models.DateTimeField(auto_now_add=True)