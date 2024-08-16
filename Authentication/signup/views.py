from django.shortcuts import render, redirect, HttpResponseRedirect
from .forms import Signup, UserEditForm, AdminEditForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.core.cache import cache
from .signals import user_registered

#DTL IMP TAG
# perms.appname.delete_modelname
#There can be edit, save in place of delete

# Create your views here.
def signup(request):
    fm = Signup()
    if request.method == "POST":
        fm = Signup(request.POST)
        if fm.is_valid():
            messages.success(request, "Account has been created!")
            user = fm.save()
            user_registered.send(sender=User, instance=user)
            group = Group.objects.get(name = "Editor")
            user.groups.add(group)
    else:
        fm = Signup()
    return render(request, "signup/signup.html",{
        "form": fm
    })

# Login function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data = request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data["username"]
                upass = fm.cleaned_data["password"]
                user = authenticate(username = uname, password=upass)
                if user is not None:
                    login(request,user) 
                    messages.success(request, "Login Successfully!")
                    return redirect("signup:profile")
        else:
            fm = AuthenticationForm()
        return render(request, "signup/login.html",{
            "form": fm})
    else:
        return redirect("signup:profile")

# Profile function
def user_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            if request.user.is_superuser == True:
                fm = AdminEditForm(request.POST, instance = request.user)
                users = User.objects.all()
            else:
                fm = UserEditForm(request.POST, instance = request.user)
                users = None
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated!")
        else:
            if request.user.is_superuser == True:
                fm = AdminEditForm(instance=request.user)
                users = User.objects.all()
            else:
                fm = UserEditForm(instance=request.user)
                users = None
        ct = cache.get('count',  version = request.user.pk)
        return render(request, "signup/profile.html",{
        "name": request.user.username, "form": fm, "users": users, "ct": ct})
    else:
        return redirect("signup:userlogin")
 
# Logout
def user_logout(request):
    logout(request)
    return redirect("signup:userlogin")

# Change password
def change_password(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user=request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Password has successfully changed")
                return redirect("signup:login")
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, "signup/change_password.html", {
            "form":fm
        })
    else:
        return redirect("signup:userlogin")

def user_detail(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(pk = id)
        fm = AdminEditForm(instance = user)
        return render(request, "signup/userdetail.html", {
            "form":fm
        })
    else:
        return redirect("signup:userlogin")