from django.db import models


class Book(models.Model):
    name = models.CharField('название книги', max_length=50)
    picture = models.ImageField('изображение')
    author = models.CharField('автор', max_length=30, default='anonymous')
    email = models.EmailField('email', blank=True)
    describe = models.TextField('описание', default='Django tutorial')

    def __str__(self):
        return self.name
