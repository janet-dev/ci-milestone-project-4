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
    """
    This view is a ListView, which retrieves a list of blog posts from
    the database with the status set to 1 (indicating published posts)
    and orders them by the created_on field in descending order.
    The view uses the 'blog/post_list.html' template to render
    the list of blog posts.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/post_list.html'


class PostDetail(generic.DetailView):
    """
    This view is a DetailView, which retrieves details of a specific
    blog post from the database based on its primary key (pk).
    The view uses the Post model and the 'blog/post_detail.html'
    template to display the detailed content of the selected blog post.
    """
    model = Post
    template_name = 'blog/post_detail.html'
