from django.urls import path
from .views import MockTestAPIView, MockTestDetailAPIView

urlpatterns = [
    path('', MockTestAPIView.as_view(), name='mock-tests-list'),
    path('<int:test_id>/', MockTestDetailAPIView.as_view(), name='mock-tests-detail'),
]