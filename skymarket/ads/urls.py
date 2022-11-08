from django.urls import include, path
from rest_framework.routers import SimpleRouter

from ads.views import AdViewSet, CommentViewSet

ads_router = SimpleRouter()
ads_router.register("ads", AdViewSet)

comments_router = SimpleRouter()
comments_router.register("comments", CommentViewSet)

urlpatterns = [
    path("api/", include(ads_router.urls), name="ads"),
    path("api/ads/<int:ad_id>/", include(comments_router.urls), name="comments"),
]
