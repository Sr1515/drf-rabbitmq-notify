from rest_framework import serializers
from .models import Post
from comments.serializers import CommentSerializer

class PostSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField('getPostComments')

    def getPostComments(self, post):
        return CommentSerializer(instance = post.getComments(), many = True, exclude = ['post']).data

    class Meta:
        model = Post
        fields = '__all__'


