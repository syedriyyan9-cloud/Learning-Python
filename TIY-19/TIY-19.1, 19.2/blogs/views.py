from django.shortcuts import render, redirect

from .models import BlogPost

from .forms import BlogForm
# Create your views here.
def home(request):
    """renders index.html"""
    blogs = BlogPost.objects.all()
    blogs = blogs.order_by('-date_added')
    context = {'blogs':blogs}
    return render(request, 'blogs/index.html',context)

def add_blog(request):
    """Adds blogs to database"""
    if request.method != 'POST':
        blog = BlogForm()
    else:
        blog = BlogForm(data = request.POST)
        if blog.is_valid():
            blog.save()
            return redirect('blogs:home')
    context = {'blog': blog}
    return render(request, 'blogs/add_blogs.html', context)

def edit_blog(request, blog_id):
    """Lets user edit existing blogs"""
    blog = BlogPost.objects.get(id = blog_id)
    if request.method != 'POST':
        form = BlogForm(instance=blog)
    else:
        form = BlogForm(instance=blog, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    context = {'form':form, 'blog':blog}
    return render(request,'blogs/edit_blogs.html',context)

         