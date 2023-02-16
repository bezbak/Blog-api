from rest_framework import generics, viewsets
from posts.models import Post
from posts.serializers import PostSerializer
# Create your views here.

class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer