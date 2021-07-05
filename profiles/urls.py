from django.urls import path
from .views import profile_update, ProfileDetailView, ProfileListView


urlpatterns = [
    path('update/', profile_update, name='profile_update'),
    path('u/<slug:slug>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('', ProfileListView.as_view(), name='profile_list'),
]
