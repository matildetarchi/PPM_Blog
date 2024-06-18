from django.urls import path
from .views import HomeView, ArticleDetailView, CreatePostView, UpdatePostView, DeletePostView, CategoryView, LikeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article'),
    path('add_post/', CreatePostView.as_view(), name='add_post'),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('categories/<str:Fashion>/', CategoryView, name='category'),
    path('like/<int:pk>', LikeView, name='like_post'),

]
