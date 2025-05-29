from django.shortcuts import render
from rest_framework import viewsets

from apps.models import Book
from apps.serializers import BookSerializer


# Create your views here.
class BookView(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving books.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

