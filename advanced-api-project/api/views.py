from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, generics, permissions
from .models import Book
from .serializers import BookSerializer

# ----------------------------
# ListView - Retrieve all books
# ----------------------------
class BookListView(generics.ListAPIView):
    """
    GET /books/
    Returns a list of all Book instances.
    Read-only access, open to any user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]  # Unauthenticated users can view

    def get_queryset(self):
        queryset = Book.objects.all()
        year = self.request.query_params.get('year')
        if year:
            queryset = queryset.filter(publication_year=year)
        return queryset


# ----------------------------
# DetailView - Retrieve a single book by ID
# ----------------------------
class BookDetailView(generics.RetrieveAPIView):
    """
    GET /books/<int:pk>/
    Returns details of a single Book instance identified by primary key (pk).
    Read-only access, open to any user.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# ----------------------------
# CreateView - Add a new book
# ----------------------------
class BookCreateView(generics.CreateAPIView):
    """
    POST /books/create/
    Creates a new Book instance.
    Restricted to authenticated users only.
    Handles data validation automatically via BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# UpdateView - Modify an existing book
# ----------------------------
class BookUpdateView(generics.UpdateAPIView):
    """
    PUT /books/update/<int:pk>/
    Updates an existing Book instance.
    Restricted to authenticated users.
    Performs full validation through BookSerializer.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# ----------------------------
# DeleteView - Remove a book
# ----------------------------
class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE /books/delete/<int:pk>/
    Deletes a Book instance identified by pk.
    Restricted to authenticated users.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
