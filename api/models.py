from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=120)
    publication_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author,related_name='books',on_delete=models.CASCADE)

    def __str__(self):
        return self.title