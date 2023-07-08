from django.contrib import admin
from django.contrib.admin import ModelAdmin

from books.models import Book, Author, Category


@admin.register(Book)
class BookModelAdmin(ModelAdmin):

    def lookups(self):
        pass

    def get_queryset(self, request):
        queryset = Book.objects.order_by('-count_view')[:10]
        return queryset


@admin.register(Author)
class AuthorModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class CategoryModelAdmin(ModelAdmin):
    pass
