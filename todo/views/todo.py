from rest_framework import serializers
from todo.models import Todo
from rest_framework import viewsets


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id',
                  'title',
                  'details',
                  'category',
                  'created',
                  )


class TodoViewSet(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
    permission_classes = []
