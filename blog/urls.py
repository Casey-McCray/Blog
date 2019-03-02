from django.urls import path
from . import views
from .views import (PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
    CommentCreateView,
    PostList
)

urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('user/<username>', UserPostListView.as_view(), name = 'user-post'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name = 'post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name = 'post-delete'),
    path('post/new/', PostCreateView.as_view(), name = 'post-create'),
    path('post/<int:p_id>/comment/', CommentCreateView.as_view(), name = 'comment-create'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/like/', PostList.as_view(), name = 'post-like'),
]
