from django.shortcuts import render, HttpResponseRedirect
from django.views import View
from .froms import ProfileForm
from .models import UserProfile
from django.views.generic.edit import CreateView
from django.views.generic import ListView
# Create your views here.
class CreateProfile(CreateView):
    template_name = "profiles/create_profile.html"
    model = UserProfile
    fields = "__all__"
    success_url = "profile"

class ProfileView(ListView):
    template_name = "profiles/user_profile.html"
    model = UserProfile
    context_object_name = "profiles"
    
    
    # def get(self, request):
    #     form = ProfileForm()
    #     return render(request, "profiles/create_profile.html", {
    #         "form": form
    #     })
    
    # def post(self, request):
    #     submitted_form = ProfileForm(request.POST, request.FILES)

    #     if submitted_form.is_valid():
    #         profile = UserProfile(image = request.FILES["user_image"])
    #         profile.save()
    #         return HttpResponseRedirect("profile")
            
    #     return render(request, "profiles/create_profile.html", {
    #         "form":  submitted_form
    #     })