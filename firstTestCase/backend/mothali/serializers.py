from rest_framework import serializers
from .models import Newsfeed

class NewsfeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsfeed
        fields =[
            'id',
            'userid',
            'title',
            'content',
            'media',
            'like',
            'dislike',
            'comments',
            'created_at',
            'updated_at',
        ]