from django.urls import path
from .views import PostCreateView, PostDeleteView, post_list


urlpatterns = [
    path('<uuid:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('', post_list, name='post_list'),
    path('new/', PostCreateView.as_view(), name='post_create'),
]