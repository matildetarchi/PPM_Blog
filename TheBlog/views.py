import warnings

from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category
from .forms import PostForm, EditForm
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'home.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context['cat_menu'] = cat_menu
        return context


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article.html'


class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'


class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')  # metti invece che rimandare li,
    # un coso che dice che è stato eliminato con successo


def CategoryView(request, Fashion):
    category_posts = Post.objects.filter(category=Fashion.replace('-', ' '))
    return render(request, 'categories.html',
                  {'Fashion': Fashion.title().replace('-', ' '), 'category_posts': category_posts})

