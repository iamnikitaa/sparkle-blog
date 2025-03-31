from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post


def home(request):
    return render(request, 'blog/home.html', {'posts': Post.objects.all()})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 5
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Home'  # Add the title here
        return context

class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    ordering = ['-date_posted'] 
    paginate_by = 5

    def get_queryset(self):
        user = User.objects.filter(username=self.kwargs.get('username')).first()
        if user:
            return Post.objects.filter(author=user).order_by('-date_posted')
        return Post.objects.none() 

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self): #checks if logges in user is the author of the post if not the access is denies
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self): #checks if logged in user is the author of the post if not the access is denies
        post = self.get_object()
        return self.request.user == post.author

    
def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})  

