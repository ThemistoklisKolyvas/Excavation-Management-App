from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExcavationViewSet, GraveViewSet


# Create a router for the viewsets
router = DefaultRouter()
router.register(r'excavations', ExcavationViewSet)
router.register(r'graves', GraveViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  # All API endpoints are prefixed with 'api/'
]


