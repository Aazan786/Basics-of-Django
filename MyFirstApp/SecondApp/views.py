from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index1(request):
    return HttpResponse("Home Page of second app!")

def home1(request):
    return HttpResponse("This is Home 1 from second app!")

def home2(request):
    return HttpResponse("This is Home 2 from second app!")

def home3(request):
    return HttpResponse("This is Home 3 from second app!")