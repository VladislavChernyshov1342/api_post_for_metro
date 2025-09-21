from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка постов.
    
    Возвращает только основные поля без лишней информации.
    Используется в GET /api/posts/
    """
    class Meta:
        model = Post
        fields = ["id", "title", "body"]


class PostDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детального просмотра поста.
    
    Включает все поля включая author_id для создания/редактирования.
    Используется в GET/POST/PUT /api/posts/{id}/
    """
    author_id = serializers.PrimaryKeyRelatedField(
        source="author", 
        queryset=Post._meta.get_field("author").remote_field.model.objects.all()
    )

    class Meta:
        model = Post
        fields = ["id", "author_id", "title", "body", "created_at", "updated_at"]




