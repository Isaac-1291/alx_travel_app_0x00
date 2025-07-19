"""
URL configuration for listings app.
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Create a router for ViewSets
router = DefaultRouter()
# router.register(r'listings', views.ListingViewSet)

app_name = 'listings'

urlpatterns = [
    # Include router URLs
    path('', include(router.urls)),
    
    # Custom API endpoints
    path('health/', views.health_check, name='health-check'),
]
