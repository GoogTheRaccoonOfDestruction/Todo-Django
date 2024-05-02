from django.db import models

# Create your models here.
class Task(models.Model):
    STATUS = [("pending", "Pending"), ("completed", "Completed")]
    TYPES = [("personal", "Personal"), ("work", "Work"), ("study", "Study")]
    PRIORITY = [("urgent", "Urgent"), ("normal", "Normal"), ("low", "Low")]
    def __str__(self):
        return self.title

    title = models.CharField(max_length=1000, null=True, blank=True)
    description = models.TextField(max_length=500)
    status = models.CharField(max_length=20, choices= STATUS, default="pending")
    type = models.CharField(max_length=20, choices= TYPES, default="personal ")
    priority = models.CharField(max_length=20, choices= PRIORITY, default="normal")