from django.urls import path, include
from . import views
from rest_framework import routers
from .views import ccsViewSet

router = routers.DefaultRouter()
router.register('ccs', ccsViewSet)

urlpatterns = [
    path('', include(router.urls)),

    # path('demo/', include('demo.urls')),

]
