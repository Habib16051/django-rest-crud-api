from django.contrib import admin
from django.urls import path, include
from app_classviews import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('apps.urls')),
    path('', include('drf_serializers.urls')),
    path('', include('app_classviews.urls')),
    path('', include('viewsets_and_routers.urls')),
    path('', views.api_root),
    path('travels/<int:pk>/highlight/', views.TravelHighlight.as_view(), name='travel-highlight'),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
