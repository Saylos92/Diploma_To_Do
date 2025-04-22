from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.hashers import make_password

from tasks.models import Task, Priority, Category, User
from .permissions import IsAdminOrTaskOwner
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer, UserSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrTaskOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(created_by=user)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriorityViewSet(ModelViewSet):
    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer

class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        password = serializer.validated_data.get("password")
        serializer.save(password=make_password(password))
