from django.shortcuts import render
from .models import Book, Library
from django.views.generic import DetailView


# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books':books})

class library_detail(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'