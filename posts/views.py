from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DeleteView, CreateView, ListView
from .models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ('body',)
    template_name = 'posts/post_create.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    template_name = 'posts/post_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class PostListView(ListView):
    model = Post
    queryset = Post.objects.prefetch_related('pictures').select_related('author').all()
    context_object_name = 'posts'
    template_name = 'posts/post_list.html'
