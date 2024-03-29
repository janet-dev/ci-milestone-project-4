'''
These unit tests have been generated by OpenAI's ChatGPT
'''

from django.contrib.auth.models import User
from django.test import SimpleTestCase, TestCase
from django.urls import resolve, reverse
from .views import PostList, PostDetail
from .models import Post


class UrlsTest(SimpleTestCase):
    '''
    This is a unit test for the urlpatterns in this Blog app
    In this example, we define two test methods:
    test_post_list_url_resolves and
    test_post_detail_url_resolves.
    These methods ensure that the URLs 'post_list' and 'post_detail'
    resolve to the correct view classes
    (PostList and PostDetail, respectively).
    '''
    def test_post_list_url_resolves(self):
        url = reverse('post_list')
        self.assertEqual(resolve(url).func.view_class, PostList)

    def test_post_detail_url_resolves(self):
        url = reverse('post_detail', args=['example-slug'])
        self.assertEqual(resolve(url).func.view_class, PostDetail)


class PostModelTest(TestCase):
    '''
    In this example, we define a test case PostModelTest that inherits
    from Django's TestCase class. We set up a test database using the
    setUpTestData method to create a Post instance for testing.
    Then, we write individual test methods to check various aspects
    of the Post model, such as field lengths, relationships,
    default values, and the string representation.
    '''
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        author = User.objects.create(username='testuser')
        Post.objects.create(
            title='Test Post',
            slug='test-post',
            author=author,
            content='This is a test post content.',
            status=1,
        )

    def test_title_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('title').max_length
        self.assertEqual(max_length, 200)

    def test_slug_max_length(self):
        post = Post.objects.get(id=1)
        max_length = post._meta.get_field('slug').max_length
        self.assertEqual(max_length, 200)

    def test_author_relationship(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.author.username, 'testuser')

    def test_default_status_value(self):
        post = Post.objects.get(id=1)
        self.assertEqual(post.status, 1)

    def test_string_representation(self):
        post = Post.objects.get(id=1)
        self.assertEqual(str(post), 'Test Post')
