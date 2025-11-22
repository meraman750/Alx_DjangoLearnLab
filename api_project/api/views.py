from django.shortcuts import render
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics
# Create your views here.


class BookList(generics.ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
