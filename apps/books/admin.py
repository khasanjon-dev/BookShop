from django.contrib import admin
from django.contrib.admin import ModelAdmin

from books.models import Book, Author, Category


@admin.register(Book)
class BookModelAdmin(ModelAdmin):
    pass


@admin.register(Author)
class BookModelAdmin(ModelAdmin):
    pass


@admin.register(Category)
class BookModelAdmin(ModelAdmin):
    pass
