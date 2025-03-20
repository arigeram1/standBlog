from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class Category(models.Model):

    title = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.title


class Article(models.Model):


    category = models.ManyToManyField(Category)

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=70)

    body = models.TextField()

    image = models.ImageField(upload_to='images/article')

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)


    # def get_absolute_url(self):
    #
    #     return reverse('')

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
