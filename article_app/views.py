from django.shortcuts import render

from .models import Category , Article




def articleDetailView(request,slug):

    article = Article.objects.get(slug=slug)

    return render(request,'article_app/article_details.html', context={'article':article})


def articleListView(request):

    articles = Article.objects.all()

    return render(request,'article_app/article_list.html', context={'articles':articles})



def articleByCatView(request,pk):

    category = Category.objects.get(id=pk)

    articles = category.articles.all()

    return render(request,'article_app/category_detail.html',context={'articles':articles})



