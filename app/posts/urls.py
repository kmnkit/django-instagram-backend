from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HashtagViewSet, PostViewSet

app_name = "posts"

router = DefaultRouter()
router.register("hashtags", HashtagViewSet)
router.register("", PostViewSet)

urlpatterns = [path("", include(router.urls))]
