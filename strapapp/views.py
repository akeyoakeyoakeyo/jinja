from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def homepage(request):
    return render(request, 'index.html')
def portpage (request):
    return render(request,'portfolio-details.html')
def servicepage(request):
    return render(request,'services-details.html')
def blogdetailpage(request):
    return render(request,'blog-details.html')
def blogpage(request):
    return render(request,'blog.html')
