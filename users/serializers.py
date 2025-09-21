from rest_framework import serializers
from .models import User


class UserListSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка пользователей.
    Минимальный набор полей для отображения в списке.
    Используется в GET /api/users/
    """
    class Meta:
        model = User
        fields = ["id", "full_name", "email"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детального просмотра пользователя.
    Полная информация включая адрес.
    Используется в GET /api/users/{id}/
    """
    class Meta:
        model = User
        fields = ["id", "full_name", "email", "address", "photo", "created_at", "updated_at"]
