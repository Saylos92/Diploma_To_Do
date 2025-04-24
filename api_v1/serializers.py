from attr.setters import validate
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from tasks.models import Task, Priority, Category, User


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "status",
            "completed",
            "created_at",
            "completed_at",
            "updated_at",
            "created_by",
            "category",
            "priority"
        ]

        read_only_fields = ["created_at", "completed_at", "updated_at", "created_by"]


class PrioritySerializer(serializers.ModelSerializer):
    class Meta:
        model = Priority
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "password",
            "first_name",
            "last_name",
            "email",
            "date_joined"
        ]
        extra_kwargs = {'password': {'write_only': True}}
        read_only_fields = ["date_joined"]

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data.get('first_name'),
            last_name=validated_data.get('last_name')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
