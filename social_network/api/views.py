from django.db.models import Count
from django.http import JsonResponse
from django.utils import timezone
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Post, Like
from .serializers import PostSerializer, LikeSerializer, UserSerializer


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer


class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


class LikeCreateView(generics.CreateAPIView):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id = serializer.validated_data['post_id']
        post = Post.objects.get(pk=post_id)
        user = self.request.user

        if user in post.likes.all():
            post.likes.remove(user)
            return Response({'message': 'Post unliked.'}, status=status.HTTP_200_OK)
        else:
            post.likes.add(user)
            return Response({'message': 'Post liked.'}, status=status.HTTP_201_CREATED)


class AnalyticsView(APIView):
    def get(self, request):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')

        if not date_from or not date_to:
            return JsonResponse({'error': 'Both date_from and date_to parameters are required.'}, status=400)

        try:
            date_from = timezone.make_aware(timezone.datetime.strptime(date_from, "%Y-%m-%d"))
            date_to = timezone.make_aware(timezone.datetime.strptime(date_to, "%Y-%m-%d"))
        except ValueError:
            return JsonResponse({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

        # Analytics about how many likes were made by day.
        analytics = Like.objects.filter(created_at__range=(date_from, date_to)) \
            .extra({'created_at_day': "date(created_at)"}) \
            .values('created_at_day') \
            .annotate(likes_count=Count('id'))

        return JsonResponse({'analytics': list(analytics)})


class UserActivityView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = self.request.user
        last_login_time = user.last_login

        return Response({
            'last_login_time': last_login_time,
        })
