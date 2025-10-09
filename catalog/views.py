from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
# Create your views here.

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # sessions
    num_visits = request.session.get('num_visits', 0)
    num_visits += 1
    request.session['num_visits'] = num_visits

    # Available books (status = 'a' )
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_visits': num_visits,
    }

    # Render HTML template index.html with data in the context variable
    return render(request, 'index.html', context=context)



class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list' # name of list as template variable
    queryset = Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war

    # for flexibility we can override methods in class based views e. g
    # def get_queryset(self):
    #     return Book.objects.filter(title__icontains='war')[:5]  # Get 5 books containing the title war

    # overriding Get_context_data
    # def get_context_data(self, **kwargs):
    #     context = super(BookListView, self).get_context_data(**kwargs)
    #     # Create any data and add it to context
    #     context['some_data'] = 'This is just some data'
    #     return context

    def get_queryset(self):
        qs = Book.objects.all()
        print("DEBUG BOOKS:", qs)  # will print to console
        return qs

#           Importnant steps of overriding    
# First get the existing context from our superclass.
# Then add your new context information.
# Then return the new (updated) context.


    template_name = 'books/book_list.html' # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book
    paginate_by = 10    # Django has inbuilt support for pagination, in the generic class-based list view
    # After 10 records the view will start paginating /catalog/books/?page=2.

    # template_name = 'books/book_detail.html' # Specify your own template name/location
