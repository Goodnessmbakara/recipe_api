from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path
from .views import MemberListCreateView, MemberDetailView

urlpatterns = [
 
    path('api/members/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/members/', MemberListCreateView.as_view(), name='member_register'),
    path('api/members/<int>:<pk>/', MemberDetailView.as_view(), name='member'),
]