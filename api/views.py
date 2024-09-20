from django.shortcuts import render
from rest_framework import generics
from .models import Blogpost
from .serializer import BlogpostSerializer


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer


class BlogPostRetriveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blogpost.objects.all()
    serializer_class = BlogpostSerializer
    lookup_field = "pk"