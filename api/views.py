from django.shortcuts import render
from .models import Author, Book
from rest_framework.decorators import api_view
from django.http import JsonResponse
from django.db.models import Q

@api_view(['GET'])
def get_books_by_author(request,author_id):
    try:
        author = Author.objects.get(id=author_id)
        books = Book.objects.filter(author=author)
        data = [
            {
                "title":book.title,
                "publication_date":book.publication_date
            }
            for book in books
        ]

        main_data = {
            "author": author.name,
            "books": data
        }

        return JsonResponse(main_data,status=200)

    except Author.DoesNotExist:
        return JsonResponse({"error":"Author not found"},status=400)


@api_view(['GET'])
def search_book(request):
    '''
    Search the books using Q objects for complex queries
    '''
    query = request.GET.get('query','')
    print(query)
    books = Book.objects.filter(Q(title__icontains=query) | Q(author__name__icontains=query))
    data = [
        {
            "title": book.title,
            "publication_date": book.publication_date,
            "author": book.author.name
        }
        for book in books

    ]

    return JsonResponse({"data":data},status=200)


