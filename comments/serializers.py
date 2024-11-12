from rest_framework import serializers
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):

    def __init__(self, *args, exclude = None, **kwargs):
        super().__init__(*args, **kwargs)
        
        if exclude is not None:
            for field in exclude:
                self.fields.pop(field)

    class Meta:
        model = Comment
        fields = '__all__'
