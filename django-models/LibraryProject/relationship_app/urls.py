from django.urls import path
from .views import books_list, library_detail

urlpatterns = [
    path('books/', books_list, name='list_books'),
    path('library/<int:pk>/', library_detail.as_view(), name='library_deatil'),
]