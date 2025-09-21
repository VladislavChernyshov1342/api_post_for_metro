from django.db import models
from users.models import User


class Post(models.Model):
    """
    Модель поста в блоге.
    
    Каждый пост привязан к автору через ForeignKey.
    Поля created_at и updated_at автоматически обновляются.
    """
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Возвращает заголовок поста для отображения в админке."""
        return self.title




