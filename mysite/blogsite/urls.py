from django.urls import path
from . import views
from .views import (
                        PostListView,
                        PostDetailView,
                        PostCreateView,
                        PostUpdateView,
                        PostDeleteView
                    )


urlpatterns = [
    # path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),  # this needs a template <app>/<model>_<viewtype>.html
                                                               # In this case, blogsite/post_list.html or mention the template name in views.py
    # Retrieve specific blog with URL pattern as /blog/<id>
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'), #name of the template for create and update is post_form.html and shared

    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]