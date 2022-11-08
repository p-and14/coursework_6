from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser

from ads.models import Ad, Comment
from ads.serializers import AdSerializer, CommentSerializer, AdDetailSerializer
from ads.filters import AdFilter
from ads.permissions import IsNotAuthenticated, IsUser

from skymarket import settings


class AdPagination(pagination.PageNumberPagination):
    page_size = settings.PAGE_SIZE


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = AdFilter
    permission_classes = [IsNotAuthenticated | IsUser | IsAdminUser]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return AdDetailSerializer
        if self.action == "create":
            return AdDetailSerializer
        return AdSerializer

    def create(self, request, *args, **kwargs):
        author = request.user

        request.data["author"] = author
        return super().create(request, *args, **kwargs)

    @action(methods=["get"], detail=False)
    def me(self, request, *args, **kwargs):
        self.queryset = Ad.objects.filter(author__email=request.user)

        return super().list(request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter()
    serializer_class = CommentSerializer
    pagination_class = AdPagination
    permission_classes = [IsNotAuthenticated | IsUser | IsAdminUser]

    def get_queryset(self):
        queryset = self.queryset.filter(ad=self.kwargs.get("ad_id", None))
        return queryset

    def create(self, request, *args, **kwargs):
        ad = self.kwargs.get("ad_id", None)
        author = request.user

        request.data["ad"] = ad
        request.data["author"] = author
        return super().create(request, *args, **kwargs)
