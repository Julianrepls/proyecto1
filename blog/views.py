from django.shortcuts import get_object_or_404, render, redirect
from django.views.generic import View, UpdateView, DeleteView
from .forms import PostCreateForm
from .models import Post
from django.urls import reverse_lazy

# Create your views here.

class BlogListView(View):
    def get(self, request, *args, **kwargs):
        posts = Post.objects.all()
        context={
            'posts':posts
        }

        return render(request, 'blog_list.html', context)
    
class BlogCreateView(View):
    def get(self, request, *args, **kwargs):

        form=PostCreateForm()
        context={
            'form':form
        }
        return render(request, 'blog_create.html', context)
    
    def post(self, request, *args, **kwargs):
        if request.method=="POST":
            form = PostCreateForm(request.POST)
            if form.is_valid():
                title = form.cleaned_data.get('title')
                content = form.cleaned_data.get('content')

                p, created = Post.objects.get_or_create(title=title, content=content)
                p.save()
                return redirect('blog:home') # lo que hace esto es que cuando hacemos un post desde post es que una vez hagamos el post pues nos redirige a home




        context={
        }
        return render(request, 'blog_create.html', context)

class BlogDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        post=get_object_or_404(Post, pk=pk)
        context={
            'post': post
        }
        return render(request, 'blog_detail.html', context)

class BlogUpdateView(UpdateView):

    model = Post
    fields=['title', 'content']
    template_name='blog_update.html'

    def get_success_url(self): # usamos esta def para qu después nos devuelva al detail blog y refresque con el kwargs pk
        pk = self.kwargs['pk'] #con esta línea de código hacemos referencia al pk que tiene el model post
        return reverse_lazy('blog:detail', kwargs={'pk':pk})
    
class BlogDeleteView(DeleteView):

    model = Post
    template_name='blog_delete.html'
    success_url=reverse_lazy('blog:home') 