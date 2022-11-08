from django.contrib.auth import get_user_model
from rest_framework import serializers


from ads.models import Ad, Comment

User = get_user_model()


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    author_image = serializers.ImageField(source="author.image", read_only=True)
    ad_id = serializers.IntegerField(source="ad.id", read_only=True)

    ad = serializers.SlugRelatedField(
        write_only=True,
        queryset=Ad.objects.all(),
        slug_field="pk"
    )

    author = serializers.SlugRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        slug_field="email"
    )

    class Meta:
        model = Comment
        fields = ["pk", "author", "text", "author_id",
                  "created_at", "author_first_name",
                  "author_last_name", "ad", "author_image", "ad_id"]


class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price", "description"]


class AdDetailSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(source="author.phone", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)

    author = serializers.SlugRelatedField(
        write_only=True,
        queryset=User.objects.all(),
        slug_field="email"
    )

    class Meta:
        model = Ad
        fields = ["pk", "image", "title", "price",
                  "phone", "description", "author_first_name",
                  "author_last_name", "author_id", "author"]
