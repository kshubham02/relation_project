from django.urls import path
from .views import *
urlpatterns = [
    path('get_books_by_author/<int:author_id>',get_books_by_author,name="get_books_by_author"),
    path('search_book/',search_book, name="search_book"),
]