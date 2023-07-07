from django.db.models import F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from books.filter import BookFilterSet
from books.models import Book
from books.pagination import CustomPageNumberPagination
from books.serializers import BookModelSerializer


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = CustomPageNumberPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = BookFilterSet

    def get_queryset(self):
        queryset = super().get_queryset()

        if not self.request.user.is_authenticated:
            queryset = queryset[:10]

        return queryset

    def list(self, request, *args, **kwargs):
        page = self.paginate_queryset(self.queryset)
        if page is not None:
            self.queryset.update(count_view=F('count_view') + 1)
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(self.queryset, many=True)
        return Response(serializer.data)
