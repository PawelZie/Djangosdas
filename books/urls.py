from django.urls import path

from books.views import get_uuids_a, get_uuids_b, get_argument_from_path, get_arguments_from_query, \
    AuthorListBaseView, raise_error_for_fun, get_headers, check_http_query_type

urlpatterns = [
    path('uuids-a', get_uuids_a),
    path('uuids-b', get_uuids_b),
    path('path-args/<int:x>/<str:y>/<slug:z>/', get_argument_from_path, name="get_from_path"),
    path('query-args/<int:x>/<str:y>/<slug:z>/', get_arguments_from_query, name="get_from_query"),
    path('check-type', check_http_query_type, name="get_from_type"),
    path('get-headers',get_headers, name="get_headers"),
    path('raise-error', raise_error_for_fun, name="raise-error"),
    path('author-list', AuthorListBaseView.as_view(), name="author-list")

]