from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
def index(request):
    #read database
    #create context variable
    my_dic = {
        "pages":['One', 'Two', 'Three','Four'],
        "courses":['Fromtemd', 'backend']}
    return render(request, "myapp/index.html", context= my_dic)

def home(request):
    return render(request, "myapp/home.html")