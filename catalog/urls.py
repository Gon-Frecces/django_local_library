# from django.urls import path
from . import views  # import views from this app
from django.urls import path, include


#For Django class-based views we access an appropriate view function by calling the class method as_view(). 
# This does all the work of creating an instance of the class, and making sure that the right handler 
# methods are called for incoming HTTP requests.

#'<int:pk> is a special syntax to capture the book id and pass it to the view as a parameter named 
# pk(primary key) which is the id being used to store the book uniquely in the DB, as defined in
# the Book model

# re_path() is just like path but it allows using regex to specify pattern e.g.
# re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'), 


]

# Django site authentication urls (for login, logout, password management)

urlpatterns += [path('accounts/', include('django.contrib.auth.urls')),
                ]