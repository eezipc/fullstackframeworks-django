from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import BlogForm
from django.urls import reverse_lazy

# Bike Blog View


class BikeBlogView(ListView):
    model = Post
    template_name = 'blog.html'

# Bike Individual Blog View


class BikeDetailView(DetailView):
    model = Post
    template_name = 'blog_detail.html'

# Add Blog View


class AddBikeBlogView(CreateView):
    model = Post
    form_class = BlogForm
    template_name = 'add_blog.html'

# Update Blog View


class UpdateBlogView(UpdateView):
    model = Post
    form_class = BlogForm
    template_name = 'edit_blog.html'

# Delete Blog View


class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('bikeblog')
