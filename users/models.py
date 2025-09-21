from django.db import models


class User(models.Model):
    """
    Модель пользователя системы.
    
    Хранит основную информацию о пользователе включая фото.
    Email должен быть уникальным в системе.
    """
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=255, blank=True)
    photo = models.ImageField(upload_to="users/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        """Возвращает строку вида 'Имя <email>' для отображения."""
        return f"{self.full_name} <{self.email}>"




