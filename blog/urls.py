from django.urls import path
from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name = 'delete'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'edit'),
    path('post/new/', BlogCreateView.as_view(), name= 'create'),
    path('', BlogListView.as_view(), name = 'home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name = 'detail'),
]