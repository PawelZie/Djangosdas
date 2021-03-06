from uuid import uuid4

import detail as detail
from IPython.core.release import authors
from django.core.exceptions import BadRequest
from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView, DeleteView

from books.forms import logger, CategoryForm, AuthorForm, BookForm
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

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))


class CategoryCreateFormView(FormView):
    template_name = "category_form.html"
    form_class = CategoryForm
    success_url = reverse_lazy("category_list")

    def form_invalid(self, form):
        logger.critical(f"FROM CRITICAL ERROR, MORE INFO {form}")
        return super().form_invalid(form)

    def form_valid(self, form):
        result = super().form_valid(form)
        logger.info(f"form = {form}")
        logger.info(f"form.cleaned_data = {form.cleaned_data}")  # cleaned means with removed html indicators
        check_entity = Category.objects.create(**form.cleaned_data)
        logger.info(f"check_entity-id={check_entity.id}")
        return result

class AuthorCreateView(CreateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author-list")

class AuthorUpdateView(UpdateView):
    template_name = "author_form.html"
    form_class = AuthorForm
    success_url = reverse_lazy("author-list")

    def get_object(self, **kwargs):
        return get_object_or_404(BookAuthor, id=self.kwargs.get("pk"))

class BookCreateView(CreateView):
    template_name = "book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("books-list")

#def get_success_url(self):
    #return reverse_lazy("book_list")

#16 z dnia 14-05-2022

class BookUpdateView(UpdateView):
    template_name = "book_form.html"
    form_class = BookForm
    success_url = reverse_lazy("books-list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))

#ciczenie z dnia 14-05
class BookDeleteView(DeleteView):
    template_name = "book_delete.html"
    model = Book
    success_url = reverse_lazy("books-list")

    def get_object(self, **kwargs):
        return get_object_or_404(Book, id=self.kwargs.get("pk"))





# 11. Utw??rz pierwsz?? funkcj?? widoku drukuj??ca/zwracaj??ca hello world (pamietaj doda?? j?? do urls.py - moesz ustawi?? jej name).




def get_hello(request: WSGIRequest) -> HttpResponse:
    hello = "hello world!"                      #nastepna cze??c zada??
    return render(request, template_name="hello_world.html", context={"hello_var": hello})

    # return HttpResponse("hello world")


# 12 Utw??rz funkcj?? zwracaj??c?? list?? string??w. Stringi niech b??d?? losowym UUID dodawanym do listy. Lista niech posiada 10 element??w.
#     a) Zwr???? list?? jako HTTPResponse (musisz na li??cie zrobi?? json.dumps)
#     b) zwr???? list?? jako JsonResponse


def get_uuids_a(request: WSGIRequest) -> HttpResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return render (request, templates_name="uuids_a.html", context={"elements": uuids})
    # return HttpResponse (f"uuids={uuids}")

def get_uuids_b(request: WSGIRequest) -> JsonResponse:
    uuids = [f"{uuid4()}" for _ in range(10)]
    return JsonResponse({f"uuids":uuids})

def get_argument_from_path(request: WSGIRequest, x: int, y: str, z: str) -> HttpResponse:


    return HttpResponse(f"X ={x}, Y = {y}, Z= {z}")

# 14. Napisz funkcj?? przyjmuj??c?? argumenty a,b,c jako zapytanie (query arguments <?> [po znaku zapytania]) i wydrukuj je

def get_arguments_from_query(request:WSGIRequest ) -> HttpResponse:
    a = request.GET.get("a")
    b = request.GET.get("b")
    c = request.GET.get("c")
    print(type(int(a)))
    return HttpResponse(f"a = {a}, b = {b}, c = {c}")

# 15. Przygotuj funkcj?? drukuj??ca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE

# 16. Przygotuj funkcj?? drukuj??ca odpowiedni komunikat dla method HTTP takich jak GET, POST, PUT, DELETE
# 17. Wykonaj zapytanie typu GET, sprawd?? czy wykonana zosta??a poprawna metoda drukuj??c jaka?? informacje w ifie.
# 18. Wykonaj zapytanie typu POST, zr??b to samo co poprzednio
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

# 21. Przygotuj funkcj?? kt??ra zwr??ci informacj?? o headerach HTTP

def get_headers(request:WSGIRequest) -> JsonResponse:
    our_headers = request.headers

    return JsonResponse({"headers":dict (our_headers)})

# 22. Rzu?? wyj??tkiem HTTP


@csrf_exempt
def raise_error_for_fun(request:WSGIRequest) -> HttpResponse:
    if not request.method != "GET":
        raise BadRequest ("method not allowed")
    return HttpResponse("wszystko GIT")

# 23. Dodaj routing w urls projektu do urls aplikacji
