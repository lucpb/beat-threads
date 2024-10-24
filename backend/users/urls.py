from django.urls import path
from .views import CustomUserCreateView, CustomUserDetailView, CustomUserUpdateView, CustomUserDeleteView

urlpatterns = [
    path('users/', CustomUserCreateView.as_view(), name='user-create'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail'),
    path('user/<int:pk>/update/', CustomUserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/delete/', CustomUserDeleteView.as_view(), name='user-delete'),
]
