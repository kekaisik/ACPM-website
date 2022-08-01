from rest_framework import serializers

from .models import Post, Event, Post_Images


class PostImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Images
        fields = ('image', )


class PostListSerializer(serializers.ModelSerializer):
    images = PostImagesSerializer(many=True)

    class Meta:
        model = Post
        depth = 1
        fields = ('title', 'text', 'main_image', 'paid', 'date', 'youtube_url', 'images')


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        exclude = ("draft", )
