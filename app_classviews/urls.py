from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    path('travel-list/', views.TravelListView.as_view(), name='travel-list'),
    path('travel-list/<int:pk>/', views.TravelDetailView.as_view(), name='travel-detail'),
    #     User related URLs
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
])
