from uuid import uuid4

import detail as detail
from IPython.core.release import authors
from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView

from books.forms import logger
from books.models import BookAuthor, Category, Book
import logging

logger = logging.getLogger("pawel")

class AuthorListBaseView(View):
    template_name = "author_list.html"
    queryset = BookAuthor.objects.all() # type: ignore

    def get(self, request: WSGIRequest, *arg, **kwargs):
        logger.debug(f"{request}-!!!")
        context = {"authors": self.queryset}
        return render(request, template_name=self.template_name, context=context)


class CategoryListTemplateView(TemplateView):
    template_name = "category_list.html"
    extra_context = {"categories": Category.objects.all()} #type: ignore


class BooksListView(ListView):
    template_name = "books_list.html"
    model = Book
    paginate_by = 10


class BooksDetailsView(DetailView):
    template_name = "book_detail.html"
    model = Book

    def get_object(self, queryset=None):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))





# 11. Utwórz pierwszą funkcję widoku drukująca/zwracająca hello world (pamietaj dodać ją do urls.py - moesz ustawić jej name).


def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "hello world!"                      #nastepna cześc zadań
    return render(request, template_name="hello_world.html", context={"hello_var": hello})

    # return HttpResponse("hello world")


# 12 Utwórz funkcję zwracającą listę stringów. Stringi niech będą losowym UUID dodawanym do listy. Lista niech posiada 10 elementów.
#     a) Zwróć listę jako HTTPResponse (musisz na liście zrobić json.dumps)
#     b) zwróć listę jako JsonResponse


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render (request, templates_name="uuids_a.html", context={"elements": uuids})
    # return HttpResponse (f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({f"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:


    return HttpResponse(f"X ={x}, Y = {y}, Z= {z}")

# 14. Napisz funkcję przyjmującą argumenty a,b,c jako zapytanie (query arguments <?> [po znaku zapytania]) i wydrukuj je

def get_arguments_from_query(request:WSGIRequest ) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int(a)))
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

# 15. Przygotuj funkcję drukująca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE

# 16. Przygotuj funkcję drukująca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE
# 17. Wykonaj zapytanie typu GET, sprawdź czy wykonana została poprawna metoda drukując jakaś informacje w ifie.
# 18. Wykonaj zapytanie typu POST, zrób to samo co poprzednio
# 19. Wykonaj zapytanie typu PUT, -||-.
# 20. Wykonaj zapytanie typu DELETE, -||-.


@csrf_exempt
def check_http_check_type(request:WSGIRequest) -> HttpResponse:
    check_type = "Unknown"
    # if request.method=="GET":
    #     check_type="to jest GET"
    # elif request.method == "POST":
    #     check_type = "to jest POST"
    # elif request.method == "PUT":
    #     check_type = "PUT"
    # elif request.method == "DELETE":
    #     check_type = "DELETE"

    # return HttpResponse(check_type)
    return render(request, template_name="methods.html",context={})


def check_http_query_type():
    return None

# 21. Przygotuj funkcję która zwróci informację o headerach HTTP

def get_headers(request:WSGIRequest) -> JsonResponse:
    our_headers = request.headers

    return JsonResponse({"headers":dict (our_headers)})

# 22. Rzuć wyjątkiem HTTP


@csrf_exempt
def raise_error_for_fun(request:WSGIRequest) -> HttpResponse:
    if not request.method != "GET":
        raise BadRequest ("method not allowed")
    return HttpResponse("wszystko GIT")

# 23. Dodaj routing w urls projektu do urls aplikacji
