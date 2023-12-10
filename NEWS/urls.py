from . import views
from .views import EditCommentView, DeleteCommentView
from django.urls import path

urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path(
        'edit/<int:comment_id>',
        EditCommentView.as_view(),
        name='edit_comment'
    ),
    path(
        'delete/<int:comment_id>',
        DeleteCommentView.as_view(),
        name='delete_comment'
    ),
]
