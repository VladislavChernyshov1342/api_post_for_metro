from django.core.management.base import BaseCommand
from django.db import transaction
from users.models import User
from posts.models import Post


class Command(BaseCommand):
    help = "Populate demo users and posts"

    @transaction.atomic
    def handle(self, *args, **options):
        users_data = [
            {"full_name": "Иван Иванов", "email": "ivan@example.com", "address": "Москва"},
            {"full_name": "Пётр Петров", "email": "petr@example.com", "address": "Санкт-Петербург"},
            {"full_name": "Сидор Сидоров", "email": "sidor@example.com", "address": "Казань"},
        ]

        created_users = []
        for data in users_data:
            user, _ = User.objects.get_or_create(email=data["email"], defaults=data)
            created_users.append(user)

        posts_data = [
            {"title": "Первый пост", "body": "Информация", "author": created_users[0]},
            {"title": "Второй пост", "body": "Информация", "author": created_users[1]},
            {"title": "Третий пост", "body": "Информация", "author": created_users[2]},
        ]

        for data in posts_data:
            Post.objects.get_or_create(
                title=data["title"],
                author=data["author"],
                defaults={"body": data["body"]},
            )

        self.stdout.write(self.style.SUCCESS("Demo data seeded successfully."))


