from rest_framework import serializers
from .models import Newsfeed,Questions

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

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = [
            'userid',
            'subject',
            'description',
            'like',
            'dislike',
            'answers',
            'created_at',
            'updated_at',
        ]

