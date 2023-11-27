from rest_framework.serializers import CurrentUserDefault, HiddenField, ModelSerializer

from .models import Task

class TaskSerializer(ModelSerializer):
    user = HiddenField(default=CurrentUserDefault())

    class Meta:
        model = Task
        fields = (
            'id',
            'user',
            'title',
            'description',
            'status',
            'created_at',
        )
        read_only_fields = ('created_at',)
        write_only_fields = ('user',)
