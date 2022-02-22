from msilib.schema import ListView
from pyexpat import model
from re import template
from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

class BookListView(ListView):
    model=Book
    template_name= 'book_list.html'
