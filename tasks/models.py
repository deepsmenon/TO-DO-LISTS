from django.db import models
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    completed_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.title = self.title.capitalize() 

        if self.completed and self.completed_date is None:
            self.completed_date = timezone.now()
        
        elif not self.completed:
            self.completed_date = None
        super().save(*args, **kwargs)


    def __str__(self):
        return self.title
