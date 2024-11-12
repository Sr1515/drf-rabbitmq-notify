from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
    def getComments(self):
        return self.comments.all()

