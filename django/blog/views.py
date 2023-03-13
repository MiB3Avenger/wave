from django.shortcuts import render
# Create your views here.

from .forms import SearchForm
#列出所有文章
from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.filter(status='published')
    return render(request, 'blog/post/list.html', {'posts': posts})
#     posts = Post.publish.all()
#     return render(request, 'blog/post/list.html', {'posts': posts})
#单独一篇
def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status="published", publish__year=year, publish__month=month,
                             publish__day=day)
    return render(request, 'blog/post/detail.html', {'post': post})

#post查找
def post_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.objects.filter(title__icontains=query)
            #results = Post.objects.annotate(search=SearchVector('title', 'slug', 'body'), ).filter(search=query)
    #return render(request, 'blog/post/search.html', {'query': query, "form": form, 'results': results})
    return render(request, 'blog/post/search.html', {'query': query, "form": form, 'results': results})








# from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.db.models import Q
#
# def user_list(request):
#     search_query = request.GET.get('search', '')
#     if search_query:
#         users = User.objects.filter(Q(username__icontains=search_query) |
#                                     Q(email__icontains=search_query))
#     else:
#         users = User.objects.all()
#
#     context = {'users': users, 'search_query': search_query}
#     return render(request, 'user_list.html', context)
#
# def user_list(request):
#     users = User.objects.all()
#     context = {'users': users}
#     return render(request, 'blog/user_list.html', context)

