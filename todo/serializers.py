from rest_framework import serializers
from .models import Task, Folder
from users.models import User
from users.serializers import UserSerializer


class FolderSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    user_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=User.objects.all(), source='user')
    class Meta:
        model = Folder
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    folder = FolderSerializer(read_only=True)
    folder_id = serializers.PrimaryKeyRelatedField(
        write_only=True, queryset=Folder.objects.all(), source='folder')

    class Meta:
        model = Task
        fields = ('id', 'title', 'completed', 'folder', 'folder_id')
