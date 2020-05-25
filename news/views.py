from django.shortcuts import render
from rest_framework import generics

from news.models import Post, Comment
from news.serializers import PostSerializer, CommentSerializer


class PostListCreateList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentCreateList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
