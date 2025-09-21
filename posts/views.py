from rest_framework import viewsets
from .models import Post
from .serializers import PostListSerializer, PostDetailSerializer


class PostViewSet(viewsets.ModelViewSet):
    """
    ViewSet для работы с постами.
    
    Поддерживает все CRUD операции:
    - GET /api/posts/ - список постов
    - POST /api/posts/ - создание поста
    - GET /api/posts/{id}/ - детали поста
    - PUT/PATCH /api/posts/{id}/ - обновление поста
    - DELETE /api/posts/{id}/ - удаление поста
    """
    queryset = Post.objects.all().order_by("-created_at")

    def get_serializer_class(self):
        """
        Выбирает сериализатор в зависимости от действия.
        
        Для списка используется PostListSerializer,
        для остальных операций - PostDetailSerializer.
        """
        if self.action == "list":
            return PostListSerializer
        return PostDetailSerializer




