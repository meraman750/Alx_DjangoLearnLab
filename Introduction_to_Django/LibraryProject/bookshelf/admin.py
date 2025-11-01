from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'author', 'pulication_year')
  search_fileds = ('title', 'author')

admin.site.register(Book, BookAdmin)
