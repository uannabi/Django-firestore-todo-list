from rest_framework import serializers
from todo.models import Category
from rest_framework import generics
from rest_framework import viewsets


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id',
                  'name',)


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = []
    authentication_classes =[]



