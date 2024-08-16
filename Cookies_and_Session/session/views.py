from django.shortcuts import render

# Create your views here.
def set_session(request):
    request.session['name'] = "Azan"
    return render(request, "session/set_session.html")

def get_session(request):
    name = request.session['name'] 
    return render(request, "session/get_session.html", {
        "name": name
    })

def del_session(request):
    request.session.flush()
    return render(request, "session/del_session.html")
