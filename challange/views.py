from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Mentor, Mentee, Blog

# Create your views here.
def index(request):
    return render(request, 'challange/index.html', {})

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'challange/blog.html', {'blogs':blogs})

def mentee(request):
    mentees = Mentee.objects.all()
    return render(request, 'challange/mentee.html', {'mentees':mentees})

def mentor(request):
    mentors = Mentor.objects.all()
    return render(request, 'challange/mentor.html', {'mentors':mentors})

def author(request):
    return render(request, 'challange/author.html', {})

def blogform(request):
    return render(request,'challange/blogform.html', {})

def submit(request):
    submitted = Blog(
        judul = request.POST['judul'],
        foto = request.POST['foto'],
        isi = request.POST['isi']
    )

    submitted.save()
    return redirect('/blog')

def seemore(request, blog_id):
    ids = Blog.objects.filter(id=blog_id)
    return render(request, 'challange/seemore.html', {'ids':ids})
    
