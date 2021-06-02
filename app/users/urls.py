from django.urls import path
from rest_framework_jwt.views import (
    obtain_jwt_token,
    verify_jwt_token,
    refresh_jwt_token,
)
from .views import (
    UserCreateViewSet,
    UserUpdateViewSet,
    UserRetrieveView,
    UserDeleteView,
    UserListView,
)

app_name = "users"

urlpatterns = [
    path("api/token/", obtain_jwt_token),
    path("api/token/verify/", verify_jwt_token),
    path("api/token/refresh/", refresh_jwt_token),
    path("", UserListView.as_view(), name="list"),
    path("create/", UserCreateViewSet.as_view(), name="create"),
    path("<int:pk>/", UserRetrieveView.as_view(), name="detail"),
    path("<int:pk>/update/", UserUpdateViewSet.as_view(), name="update"),
    path("<int:pk>/delete/", UserDeleteView.as_view(), name="delete"),
]
