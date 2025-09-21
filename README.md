Django REST API для работы с пользователями и постами.

## Быстрый старт

```bash
# 1. Создать venv и установить зависимости
python -m venv .venv
.venv\Scripts\activate
pip install -r api_post_for_metro/requirements.txt

# 2. Применить миграции
python api_post_for_metro/manage.py makemigrations
python api_post_for_metro/manage.py migrate

# 3. Запустить сервер
python api_post_for_metro/manage.py runserver
```

Сервер: http://127.0.0.1:8000/

## API Эндпоинты

- `GET/POST /api/users/` - пользователи
- `GET/PUT/DELETE /api/users/{id}/` - пользователь по ID
- `GET/POST /api/posts/` - посты  
- `GET/PUT/DELETE /api/posts/{id}/` - пост по ID
