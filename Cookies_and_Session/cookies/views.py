from django.shortcuts import render

# Create your views here.

# Cookies can be created with --> set_signed_cookie() for additional security

def set_cookies(request):
    response = render(request, "cookies/set_cookie.html")
    response.set_cookie("name", "Azan")
    return response

def get_cookies(request):
    # name = request.COOKIES["name"]
    name = request.COOKIES.get("name")
    return render(request, "cookies/get_cookie.html", {
        "name": name
    })


def del_cookies(request):
    response = render(request, "cookies/del_cookie.html")
    response.delete_cookie("name")
    return response

