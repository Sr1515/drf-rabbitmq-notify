from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Comment
from .serializers import CommentSerializer
from posts.models import Post
from .tasks import send_notification

class CommentView(APIView):
    
    def post(self, request, post_id):
        post = Post.objects.get(id=post_id)
        comment_data = request.data
        comment_data['post'] = post.id
        serializer = CommentSerializer(data=comment_data)
        
        if serializer.is_valid():
            comment = serializer.save()
            send_notification.delay(post.author, comment.author, post.title)
            return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

