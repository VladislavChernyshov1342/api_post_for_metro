from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "body"]


class PostDetailSerializer(serializers.ModelSerializer):
    author_id = serializers.PrimaryKeyRelatedField(source="author", queryset=Post._meta.get_field("author").remote_field.model.objects.all())

    class Meta:
        model = Post
        fields = ["id", "author_id", "title", "body", "created_at", "updated_at"]


