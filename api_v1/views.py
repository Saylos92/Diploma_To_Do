from rest_framework.viewsets import ModelViewSet
from django.utils import timezone

from tasks.models import Task, Priority, Category, User
from .permissions import IsAdminOrTaskOwner, IsAdminOrReadOnly
from .serializers import TaskSerializer, CategorySerializer, PrioritySerializer, UserSerializer


class TaskViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = (IsAdminOrTaskOwner,)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Task.objects.all()
        return Task.objects.filter(created_by=user, deleted=False)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        completed = serializer.validated_data.get("completed")
        if completed:
            return serializer.save(completed_at=timezone.now())
        if completed == False:
            return serializer.save(completed_at=None)
        serializer.save(updated_at=timezone.now())

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.deleted_at = timezone.now()
        instance.save()


class CategoryViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class PriorityViewSet(ModelViewSet):
    permission_classes = (IsAdminOrReadOnly,)

    queryset = Priority.objects.all()
    serializer_class = PrioritySerializer


class UsersViewSet(ModelViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return User.objects.all()
        return User.objects.filter(username=user)
