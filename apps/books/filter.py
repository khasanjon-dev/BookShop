from django_filters import FilterSet, NumberFilter

from books.models import Book


class BookFilterSet(FilterSet):
    from_price = NumberFilter('price', 'gte')
    to_price = NumberFilter('price', 'lte')

    class Meta:
        model = Book
        fields = {
            'title': ['exact'],
            'category': ['exact'],
            'author': ['exact'],
            'price': ['exact'],
            'year': ['exact']
        }
