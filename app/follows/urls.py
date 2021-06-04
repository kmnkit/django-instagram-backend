from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FollowViewSet

app_name = "follows"

router = DefaultRouter()
router.register("", FollowViewSet)

urlpatterns = [path("", include(router.urls))]
