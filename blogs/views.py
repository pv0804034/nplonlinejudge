from django.shortcuts import render
from blogs.models import Blog
from django.http import HttpResponseNotFound
# Create your views here.


def blogdetails(request, _id):
    blog = Blog.objects.filter(id=_id)
    if blog.exists():
        blog = blog[0]
    else:
        return HttpResponseNotFound()
    return render(request, 'blogs/blogdetails.html', {'blog': blog})


def blogs(request):
    blogs = Blog.objects.all().order_by('-when')
    for idx, blog in enumerate(blogs):
        blog.serial = idx + 1
    return render(request, 'blogs/blogs.html', {'blogs': blogs})
