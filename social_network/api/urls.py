from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import PostListCreateView, AnalyticsView, LikeCreateView, UserSignupView, UserActivityView

urlpatterns = [
    path('signup/', UserSignupView.as_view(), name='user-signup'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('like/', LikeCreateView.as_view(), name='like-create'),
    path('analytics/', AnalyticsView.as_view(), name='analytics'),
    path('activity/', UserActivityView.as_view(), name='user-activity'),
]
