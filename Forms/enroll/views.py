from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import StudentRegistration
from django.contrib import messages
# Create your views here.

def showformdata(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST, auto_id=True)
        if fm.is_valid():
            fm.save()
            # messages.add_message(request, messages.SUCCESS, "Your account has been created!")
            messages.info(request, "You can login!")
            print(messages.get_level(request))
            messages.debug(request, "Error in code")
            messages.set_level(request, messages.DEBUG)
            messages.debug(request, "New Error in code")
            print(messages.get_level(request))
            #return HttpResponseRedirect("success")

    else:
        fm = StudentRegistration()
        print("Get Request")

    return render(request, "enroll/student.html", {
        "form": fm
    })

def thankyou(request):
    return render(request, "enroll/success.html")