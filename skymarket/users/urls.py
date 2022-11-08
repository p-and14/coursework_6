from django.urls import include, path
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

user_router = SimpleRouter()
user_router.register("users", UserViewSet, basename="users")

urlpatterns = [
    path("api/", include(user_router.urls), name="users"),
    path("api/token/", TokenObtainPairView.as_view(), name="jwt-create"),
    path("refresh/", TokenRefreshView.as_view(), name="jwt-refresh"),
]
