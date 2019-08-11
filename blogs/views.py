from django.shortcuts import render

# Create your views here.


def blogdetails(request):
    return render(request, 'blogs/blogdetails.html', {'data': data})


def blogs(request):
    data = dict()
    return render(request, 'blogs/blogs.html', {'data': data})
