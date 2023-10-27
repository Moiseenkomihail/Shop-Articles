from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from django.views.generic import CreateView,DetailView, ListView, UpdateView
from .models import *
from django.contrib.auth.mixins import PermissionRequiredMixin


class CreateArticleView(PermissionRequiredMixin,CreateView):
    permission_required = 'articles.add_articles'
    model = Articles
    fields = ('name', 'content')
    template_name = 'articles/createarticle.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.newswriter = self.request.user
        return super().form_valid(form)

class ArticleListView(ListView):
    model = Articles
    fields = ('name', 'newswriter')
    context_object_name = 'articles'
    template_name = 'articles/articles.html'



# class DetailArticleView(DetailView):
#     model = Articles
#     field = ('name', 'newswrier', 'content')
#     context_object_name = 'article'
#     template_name = 'articles/article.html'

# class UpdateArticleView(PermissionRequiredMixin, UpdateView):
#     model = Articles
#     fields = [
#         'name',
#         'content'
#     ]

def DetailArticleView(request, id):
    template_name = 'articles/article.html'
    article = get_object_or_404(Articles, pk=id)
    comments = ArticleComment.objects.filter(article_id = id)
    new_comment = None
    comments_form = ArticleCommentForm()
    if request.method == 'POST':
        comments_form = ArticleCommentForm(data=(request.POST or None))
        if comments_form.is_valid():   
            data = request.POST.get('comment')
            new_comment = ArticleComment.objects.create(article = article, writer = request.user, comment = data)
            return redirect(article.get_absolute_url())
        else:
            comments_form = ArticleCommentForm()
    context = {
        'comment_form': comments_form,
        'comments':comments,
        'article': article
    }
    return render(request, template_name, context)
    
        