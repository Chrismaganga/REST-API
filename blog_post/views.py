from django.shortcuts import render
from django.shortcuts import get_object_or_404
from blog_post.serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from blog_post.models import Post

class PostViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving posts.
    """
    def list(self, request):
        queryset = Post.objects.all()
        serializer = PostSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Post.objects.all()
        post = get_object_or_404(queryset, pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
