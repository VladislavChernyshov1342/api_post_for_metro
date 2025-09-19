from rest_framework import viewsets
from .models import User
from .serializers import UserListSerializer, UserDetailSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by("-created_at")
    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        return UserDetailSerializer


