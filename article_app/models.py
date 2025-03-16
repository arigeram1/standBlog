from django.db import models

from django.contrib.auth.models import User


# همیشه کلاسی که داره یک فیلد فارین رو میاره میره اول معادله یعنی

# many to one

# یعنی جدول آرتیکل منی محسوب میشه و جدولی که بهش مرتبط میشه میشه وان

# یعنی چند مقاله مرتبط میشوند به یک کاربر

class Article(models.Model):

    author = models.ForeignKey(User,on_delete=models.CASCADE)

    title = models.CharField(max_length=70)

    body = models.TextField()

    image = models.ImageField(upload_to='images/article')

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'
