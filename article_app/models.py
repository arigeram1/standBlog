from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.text import slugify

from account_app.models import Profile

class Category(models.Model):

    title = models.CharField(max_length=100 , verbose_name='عنوان')

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.title

    class Meta:

        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Article(models.Model):

    category = models.ManyToManyField(Category , related_name='articles' ,verbose_name='دسته بندی')

    author = models.ForeignKey(User,on_delete=models.CASCADE , related_name='articles',verbose_name='نویسنده')

    title = models.CharField(max_length=70,verbose_name='عنوان مقاله')

    body = models.TextField(verbose_name='متن مقاله')

    image = models.ImageField(upload_to='images/article',verbose_name='تصویر مقاله')

    created = models.DateTimeField(auto_now_add=True , verbose_name='زمان ایجاد')

    updated = models.DateTimeField(auto_now=True)

    slug = models.SlugField(unique=True , blank=True)

    status = models.BooleanField(default=False , verbose_name='فعال')

    def show_image(self):

        if self.image:

            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')

        return format_html('<h3 style="color: red">تصویر ندارد</h3>')


    show_image.short_description = 'تصویر'


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


    def getEmail(self):

        return self.author.email

    getEmail.short_description = 'ایمیل'


    def getArticle(self):

        return format_html(f'<a href="/admin/article_app/article/{self.article.id}">{self.article.title}</a>')

    getArticle.short_description = 'مقاله'


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


class Like(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE , related_name='likes' , verbose_name='کاربر')

    article = models.ForeignKey(Article,on_delete=models.CASCADE , related_name='likes', verbose_name='مقاله')

    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return f'{self.user.username} - {self.article.title}'


    class Meta:

        verbose_name = 'لایک'
        verbose_name_plural = 'لایک ها'

        ordering = ('-created_at',)





