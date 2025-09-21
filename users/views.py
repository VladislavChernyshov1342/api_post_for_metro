from rest_framework import viewsets
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с пользователями.
    Поддерживает все CRUD операции:
    - GET /api/users/ - список пользователей
    - POST /api/users/ - создание пользователя
    - GET /api/users/{id}/ - детали пользователя
    - PUT/PATCH /api/users/{id}/ - обновление пользователя
    - DELETE /api/users/{id}/ - удаление пользователя
    """
    queryset = User.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        """
        Выбирает сериализатор в зависимости от действия.
        Для списка используется UserListSerializer,
        для детального просмотра - UserDetailSerializer.
        """
        if self.action == "list":
            return UserListSerializer
        return UserDetailSerializer
