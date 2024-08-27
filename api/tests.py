


from django.test import TestCase
from .models import Book, Author
from django.urls import reverse


class BookAPITestCase(TestCase):
    def setUp(self):
        # Setup initial data
        self.author = Author.objects.create(name="williams")
        self.book = Book.objects.create(title="Book 1",author=self.author)
        self.book2 = Book.objects.create(title="Book 2",author=self.author)

    def test_get_books_by_author(self):
        url = reverse("get_books_by_author",args=[self.author.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)
        self.assertContains(response,self.book.title)
        self.assertContains(response, self.book2.title)

class SearchBookAPITestCase(TestCase):
    def setUp(self):
        # Setup initial data
        self.author = Author.objects.create(name="J. K. Rowling")
        self.book = Book.objects.create(title="Harry Potter and the Philosopher's Stone",author=self.author)
        self.book2 = Book.objects.create(title="The running Grave",author=self.author)

    def test_search_book(self):
        url = reverse('search_book')
        response = self.client.get(url,{'query':'K.'})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.book.title)
        self.assertContains(response, self.book2.title)







