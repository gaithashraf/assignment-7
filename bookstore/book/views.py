from django.shortcuts import render, HttpResponse,HttpResponseRedirect,reverse
from .forms import BookForm
from .models import Book
from django.views.generic import CreateView,DeleteView,UpdateView,ListView
from django.urls import reverse_lazy


# Create your views here.

class BookList(ListView):
    model = Book
    context_object_name = "books"
    template_name = "homepage.html"

class BookCreate(CreateView):
    model = Book
    form_class = BookForm
    success_url =reverse_lazy("homepage")
    template_name = "add_update.html"

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy("homepage")
    def get(self,request,*args,**kwargs):
        return self.delete(request,*args,**kwargs)

class BookUpdate(UpdateView):
    model = Book
    form_class = BookForm
    success_url =reverse_lazy("homepage")
    template_name = "add_update.html"
