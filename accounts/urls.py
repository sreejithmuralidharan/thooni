from django.urls import path, include

from .views import (
ProfileDetailView,
)

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('profile/<pk>/',ProfileDetailView.as_view(), name = 'profile-detail'),
    # path('profile/<pk>/update/',ProfileUpdateView.as_view(), name = 'profile-update'),
    # path('signup/', SignupCreateView.as_view(), name="signup"),
    
]
