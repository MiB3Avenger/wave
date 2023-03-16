from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=255)
    posted_at = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='otheruser', blank=True)
    likes_count = models.IntegerField(blank=True, default=0) 
    
    
    def __str__(self):
        return self.body


    class Meta:
         ordering = ('-posted_at',)
         
         
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField(max_length=200)
    commented_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.body + str(self.post)
    
    class Meta:
        ordering = ('-commented_at',)