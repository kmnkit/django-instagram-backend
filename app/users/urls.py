from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)
from .views import UserViewSet

app_name = "users"

router = DefaultRouter()
router.register("", UserViewSet)

urlpatterns = [
    path("api/token/", obtain_jwt_token),
    path("api/token/verify/", verify_jwt_token),
    path("api/token/refresh/", refresh_jwt_token),
    path("", include(router.urls)),
]
