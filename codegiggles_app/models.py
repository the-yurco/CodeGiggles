from django.db import models
from django.contrib.auth.models import User

class Snippet(models.Model):
  title = models.CharField(max_length=255)
  code = models.TextField()
  language = models.CharField(max_length=50)
  description = models.TextField(default='')
  created_at = models.DateTimeField(auto_now_add=True)
  likes = models.PositiveIntegerField(default=0)
  dislikes = models.PositiveIntegerField(default=0)

  def __str__(self):
    return self.title

