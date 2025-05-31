from django.urls import path
from . import views

urlpatterns = [
    path('api_list/', views.TravelListView.as_view()),
    path('api_list/<int:pk>/', views.TravelDetailView.as_view()),

]