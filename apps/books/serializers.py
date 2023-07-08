from rest_framework.serializers import ModelSerializer, Serializer

from books.models import Book


class BookModelSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
