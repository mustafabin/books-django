from django.db import models


BOOK_SUBJECTS = [
    ('SCI', 'Science'),
    ('FIC', 'Fiction'),
    ('NON', 'Non-Fiction'),
]


class Book(models.Model):
    title = models.CharField(max_length=128)
    subject = models.CharField(max_length=5, choices=BOOK_SUBJECTS)

    def __str__(self):
        return f'{self.subject} - {self.title}'
