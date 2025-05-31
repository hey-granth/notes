from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    id = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.title