from django.db import models

# Create your models here.
class Task(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default="pending")