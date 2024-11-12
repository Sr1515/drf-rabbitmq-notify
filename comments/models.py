from django.db import models
from posts.models import Post

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.CharField(max_length=255)

    def __str__(self):
        return f"Comentário de {self.author} no post {self.post.title}"

