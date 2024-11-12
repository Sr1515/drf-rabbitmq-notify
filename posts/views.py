from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Post
from .serializers import PostSerializer

class PostView(APIView):

    def get(self, resquest):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many = True)
        return Response(serializer.data)
    
    def post(self, request): 
        serializer = PostSerializer(data = request.data)
        
        if serializer.is_valid():
            post = serializer.save()
            return Response(PostSerializer(post).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)