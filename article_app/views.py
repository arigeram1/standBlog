from django.shortcuts import render,redirect

from .models import Category , Article,Comment

from django.core.paginator import Paginator

from django.views.generic import ListView,DetailView

from django.views.generic.base import TemplateView

def articleDetailView(request,slug):

    article = Article.objects.get(slug=slug)

    if request.method == 'POST':

        body = request.POST.get('body')

        author = request.user

        parent_id = request.POST.get('parent_id')

        Comment.objects.create(body=body,author=author,article=article,parent_id=parent_id)

    return render(request,'article_app/article_details.html', context={'article':article} )


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


def searchView(request):

    searched_value = request.GET.get('q')

    articles = Article.objects.filter(title__icontains=searched_value)

    if len(articles) > 2:

        paginator = Paginator(articles,2)

        selected_page = request.GET.get('page')

        objects_list = paginator.get_page(selected_page)

        return render(request, 'article_app/article_list.html', context={'articles': objects_list})



    return render(request,'article_app/article_list.html', context={'articles':articles})



# class ListView(View):
#
#     queryset = None
#     template_name = None
#
#     def get(self,request):
#
#         return render(request,self.template_name,{'articles':self.queryset})





class ArticleListView(ListView):

    queryset = Article.objects.all()

    template_name = 'article_app/article_list.html'



# class SingleArticleView(TemplateView):
#
#     template_name = 'article_app/article_list2.html'
#
#     def get_context_data(self, **kwargs):
#
#         context = super().get_context_data(**kwargs)
#
#         context['article'] = Article.objects.get(title__icontains='donec')
#
#         return context


