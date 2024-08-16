from django import forms
from .models import Reviews

# class Reviewform(forms.Form):
#     user_name = forms.CharField(label="Your name", max_length=10,required=True, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Please enter shorter name"
#     })
#     review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=100)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)

class  Reviewform(forms.ModelForm):
    class Meta:
        model =  Reviews
        fields = "__all__"
        labels = {
            "user_name":  "Your Name",
            "review_text": "Your Feedback",
            "rating": "Rating",
        }

        error_messages = {
            "user_name": {
                "required": "Your name must not be empty",
                "max_length": "Please enter shorter name"
            }
        }