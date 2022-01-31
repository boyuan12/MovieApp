from django.db import models

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    movie_id = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
