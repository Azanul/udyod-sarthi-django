from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import RegisterView, EndUserListCreateView, EndUserRetrieveUpdateDestroyView


urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('endusers/', EndUserListCreateView.as_view(), name='enduser-list-create'),
    path('endusers/<int:pk>/', EndUserRetrieveUpdateDestroyView.as_view(), name='enduser-retrieve-update-destroy'),
]
