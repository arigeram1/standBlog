from django.shortcuts import render

from article_app.models import Article

from account_app.models import Profile

def home(request):

    articles = Article.objects.all()

    return render(request, 'home_app/home.html', context={'articles':articles})




