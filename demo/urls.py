from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ccsViewSet, childrenViewSet, parentViewSet

router = routers.DefaultRouter()
router.register('ccs', ccsViewSet, childrenViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('demo/', include('demo.urls')),

]
