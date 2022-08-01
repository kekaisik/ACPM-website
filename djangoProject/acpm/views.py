from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post
from .serializers import PostListSerializer


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.filter(draft=False)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)


class PostDetailView(APIView):

    def get(self, request, category, tag):
        posts = Post.objects.filter(category=category, tags=tag)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
