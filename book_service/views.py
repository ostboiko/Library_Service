from rest_framework import viewsets

from book_service.models import Book


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.object.all()
    serializer_class = BookSerializer
