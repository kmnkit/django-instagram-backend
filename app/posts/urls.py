from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HashtagViewSet, PostViewSet

app_name = "posts"

router = DefaultRouter()
router.register("", PostViewSet)
router.register("hashtags", HashtagViewSet)

urlpatterns = [path("", include(router.urls))]
