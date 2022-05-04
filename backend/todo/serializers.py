from rest_framework.serializers import ModelSerializer

from todo.models import Todo


class TodoSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
        # fields = ['id', 'name', 'date_add', 'date_update', 'is_done']
