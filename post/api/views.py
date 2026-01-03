from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from post.models import Post
from post.api.serializers import PostSerializer
from post.api.permissions import IsAuthorOrReadOnly  # öz permission class-ın

class PostViewSet(ModelViewSet):
    queryset = Post.objects.filter(is_draft=False)
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
