from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse


# Create your views here.

def index(request):
    return HttpResponse("Home Page!")

def home1(request):
    return HttpResponse("This is Home 1!")

def home2(request):
    return HttpResponse("This is Home 2!")

def home3(request):
    #return HttpResponse("This is Home 3!")
    return redirect("SecondApp:home1")

def home4(request):
    my_dic= {
        "Name": "Azan",
        "Age" : 23
    }
    return JsonResponse(my_dic)