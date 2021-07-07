from django.urls import path
from .views import PostCreateView, PostDeleteView, PostListView, post_like


urlpatterns = [
    path('<uuid:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('<uuid:pk>/like', post_like, name='post_like'),
    path('', PostListView.as_view(), name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
]