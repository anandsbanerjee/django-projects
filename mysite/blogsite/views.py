from datetime import datetime
from .models import Post
from django.views.generic import (
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView
                                )
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# dummy data as dictionary - not using it as its now coming from DB
# posts = [
#     {
#         'author': 'Anand B',
#         'title': 'Blogsite-1',
#         'content': 'Blogsite - First post',
#         'date_posted': datetime.now(),
#     },
#     {
#         'author': 'Nilay B',
#         'title': 'Blogsite - 2',
#         'content': 'Blogsite - Second post',
#         'date_posted': datetime.now(),
#     }
# ]

posts = Post.objects.all()

#This is an example of function based views
def home(request):
    context = {
                'posts': posts
            }
    return render(request, 'blogsite/home.html', context) # pass data into the template

# Rewrite the home view using class based list views as its best represented as a list
class PostListView(ListView):
    model = Post  # this model will be queried
    template_name = 'blogsite/home.html'
    context_object_name = 'posts' # this will let continue to use the context variable posts that is
                                # used in the home template otherwise it will look for post_list
    ordering = ['-date']  # - sign says newest to oldeest


def about(request):
    # return HttpResponse("<h1>Blog About</h1>")
    # send the context as a dictionary directly to test condition logic for title
    return render(request, 'blogsite/about.html', {'title': 'About'})

# This class view will stick to conventions i.e. <app>/<model>_<viewtype>.html i.e. post_detail.html
class PostDetailView(DetailView):
    model = Post
# Create a post
class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']  # to be entered by user in the form

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

#for update blog post
class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDeleteView(DeleteView):
    model = Post
    success_url = '/blog/'