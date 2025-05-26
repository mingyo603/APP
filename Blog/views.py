from django.shortcuts import render
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import viewsets
from .models import Blog, BlogImage
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.

class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

from rest_framework import generics, filters

class BlogSearchView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'body']  # 검색 대상 필드들
