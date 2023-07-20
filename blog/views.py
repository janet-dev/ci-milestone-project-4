"""
    Creates 2 views: a list of blogs and a selected blog detail page

    Credit:
    Djangocentral - Building A Blog Application With Django
    by Abhijeet Pal
    https://djangocentral.com/building-a-blog-application-with-django/
"""
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
