from rest_framework import viewsets, permissions, generics, status
from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from accounts.models import CustomUser
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from notifications.models import Notification


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(author__in=following_users).order_by('-created_at')

from rest_framework import status, generics, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from .models import Post, Like
from .serializers import LikeSerializer
from notifications.models import Notification
from accounts.models import CustomUser

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if created:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)
    else:
        return Response({'status': 'already liked'}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    
    try:
        like = Like.objects.get(user=request.user, post=post)
        like.delete()
        return Response({'status': 'unliked'}, status=status.HTTP_200_OK)
    except Like.DoesNotExist:
        return Response({'status': 'not liked'}, status=status.HTTP_200_OK)
