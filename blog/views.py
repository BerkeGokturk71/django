from django.shortcuts import render
from .models import Post
from denek.models import Denek
def index(request):
    courses = Post.objects.order_by("-date")
    deneks = Denek.objects.filter(is_valid=True).order_by("-date")
    context = {
        "courses":courses,
        "deneks":deneks,
    }
    return render(request, "index.html",context)

def course_detail(request,category_slug,course_id):
    course = Post.objects.get(category__slug=category_slug,id=course_id)
    context ={
        "course":course
    }
    return render(request,"couses.html",context)

def category_detail(request,category_slug):
    courses = Post.objects.all().filter(tags__slug=category_slug)
    context ={
        "courses":courses
    }
    return render(request,"couse.html",context)

def comment(request):
    if request.method == "POST":
        name = request.POST["fullname"]
        message = request.POST["message"]

