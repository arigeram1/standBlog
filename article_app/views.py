from django.shortcuts import render

from .models import Category , Article

from django.core.paginator import Paginator


def articleDetailView(request,slug):

    article = Article.objects.get(slug=slug)

    return render(request,'article_app/article_details.html', context={'article':article})


def articleListView(request):

    articles = Article.objects.all().order_by('-created')

    paginator = Paginator(articles, 1)

    selected_page = request.GET.get('page')

    objects_list = paginator.get_page(selected_page)

    return render(request, 'article_app/article_list.html', context={'articles': objects_list})




def articleByCatView(request,pk):

    category = Category.objects.get(id=pk)

    articles = category.articles.all()

    return render(request,'article_app/category_detail.html',context={'articles':articles})



