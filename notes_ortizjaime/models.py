from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")
    title = models.CharField(max_length = 200)
    content = models.TextField()
    creation_date = models.DateTimeField("Creation date",auto_now_add=True)

    def __str__(self):
        return self.title


