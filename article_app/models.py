from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify

from account_app.models import Profile

class Category(models.Model):

    title = models.CharField(max_length=100)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.title

    class Meta:

        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):

    category = models.ManyToManyField(Category , related_name='articles')

    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name='articles')

    title = models.CharField(max_length=70)

    body = models.TextField()

    image = models.ImageField(upload_to='images/article')

    created = models.DateTimeField(auto_now_add=True)

    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True , blank=True)

    # class Meta:
    #     ordering = ('-created',)

    def save(self,force_insert = False, force_update = False,using = None,update_fields = None,):

        self.slug = slugify(self.title)

        super(Article,self).save()

    def get_absolute_url(self):

        return reverse('article_app:detail',kwargs={'slug':self.slug})

    def __str__(self):
        return f'{self.title} - {self.body[:30]}'

    class Meta:

        verbose_name = 'مقاله'
        verbose_name_plural = 'مقالات'


class Comment(models.Model):

    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='comments')

    article = models.ForeignKey(Article,on_delete=models.CASCADE , related_name='comments')

    created_at = models.DateTimeField(auto_now_add=True)

    parent = models.ForeignKey('self' , on_delete=models.CASCADE , related_name='replies' , null=True , blank=True)

    body = models.TextField()


    def __str__(self):

        return self.body[:30]

    class Meta:

        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Message(models.Model):


    title = models.CharField(max_length=100)

    body = models.TextField()

    email = models.EmailField()

    created_at = models.DateTimeField(auto_now_add=True)

    age = models.IntegerField(default=0)

    def __str__(self):

        return self.title

    class Meta:

        verbose_name = 'پیام'
        verbose_name_plural = 'پیام ها'






