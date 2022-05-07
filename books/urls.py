from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_arguments_from_query, \
    AuthorListBaseView, raise_error_for_fun, get_headers, check_http_query_type, CategoryListTemplateView, \
    BooksListView, BooksDetailsView, CategoryCreateFormView, AuthorCreateView, AuthorUpdateView


class BooksListTemplateView:
    pass


urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args', get_arguments_from_query, name="get_from_query"),
    path('query-type', check_http_query_type, name="get_query_type"),
    path('get-headers',get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name="raise-error"),
    path('author-list', AuthorListBaseView.as_view(), name="author-list"), # pierwsze author-list wpisujemy do przeglądarki , A drugie odwołujemy sie w kodzie(to co szuka django)
    path('category-list', CategoryListTemplateView.as_view(), name="category_list"),
    path('books-list', BooksListView.as_view(), name="books-list"),
    path('book-details/<int:pk>/', BooksDetailsView.as_view(), name="book-detail"),
    path('category-create', CategoryCreateFormView.as_view(), name="category_create"),
    path('author-create', AuthorCreateView.as_view(), name="author_create"),
    path('author-update/<int:pk>/', AuthorUpdateView.as_view(), name="author_update")

]