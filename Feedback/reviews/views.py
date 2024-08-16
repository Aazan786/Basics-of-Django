from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import View
from .forms import Reviewform
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, FormView
from .models import Reviews
from django.urls import reverse


# Create your views here.
class ReviewView(FormView):
    form_class = Reviewform
    template_name =  "reviews/review.html"
    success_url = "/thank_you"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def get(self, request):
    #     form = Reviewform()
           
    #     return render(request, "reviews/review.html", {
    # "form": form
    # })

    # def post(self, request):
    #     form = Reviewform(request.POST)

    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("thank_you")

    #     return render(request, "reviews/review.html", {
    # "form": form
    # })

class ThankYou(TemplateView):
    template_name = "reviews/thank_you.html"
    # def get(self, request):
    #       return render(request, "reviews/thank_you.html")

class ReviewList(ListView):
    template_name = "reviews/review_list.html"
    model = Reviews
    context_object_name = "reviews"
    ordering = ['id']
    paginate_by = 2
    
class SingleReview(DetailView):
    template_name = "reviews/single_review.html"
    model = Reviews

class AddToFavorite(View):
    def POST(self, request, pk):
        review_id = request.POST['review_id']
        request.session['fav'] =  review_id
        return redirect("reviews:fav" + review_id)

class AddToFavorite(View):
    def post(self, request, pk):
        review_id = request.POST['review_id']
        fav_review = Reviews.objects.get(pk=review_id)
        request.session['fav'] = review_id
        return redirect(reverse("reviews:single_review", kwargs={"pk": pk}))

def del_session(request):
    request.session.flush()
    return render(request, "reviews/review.html")

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     review_id = kwargs["id"]
    #     selected_review = Reviews.objects.get(pk = review_id)
    #     reviews =  Reviews.objects.all()
    #     context["reviews"] = selected_review
    #     return context

# def review(request):
#     if request.method == "POST":
#         # existing_data = Reviews.objects.get(pk=1)
#         form = Reviewform(request.POST)

#         if form.is_valid():
#             form.save()
#             # review = Reviews(
#             # user_name=form.cleaned_data['user_name'],
#             # review_text=form.cleaned_data['review_text'],
#             # rating=form.cleaned_data['rating'])
#             # review.save()
#             return HttpResponseRedirect("thank_you")
            
#     else:
#         form = Reviewform()
           
#     return render(request, "reviews/review.html", {
#     "form": form
#     })

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")