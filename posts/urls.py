from django.urls import path
from .views import PostCreateView, PostDeleteView, PostListView


urlpatterns = [
    path('<uuid:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
]