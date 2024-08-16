from django.core import validators
from django import forms
from .models import User

# class StudentRegistration(forms.Form):
#     error_css_class = 'error'
#     required_css_class = 'required'
#     name = forms.CharField(label="Your Name", label_suffix=" ", error_messages={"required": "Enter your name please"}, min_length=5, max_length=10)
#     email = forms.EmailField(label="Your Email", label_suffix=" ", error_messages={"required": "Enter your email please"})
#     pwd = forms.CharField(widget=forms.PasswordInput, error_messages={"required": "Enter your password please"})



    # def clean(self):
    #     cleaned_Data = super().clean()
    #     pwd = self.cleaned_data['password']
    #     cpwd = self.cleaned_data['confirm_password']

    #     if pwd != cpwd:
    #         raise forms.ValidationError("Password does not match")





    # def clean(self):
    #     cleaned_Data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']

    #     if len(valname) < 4:
    #         raise forms.ValidationError("Name should be greater than 4 character")
    #     if len(valemail) < 10:
    #         raise forms.ValidationError("email should be greater than 10 character")


class StudentRegistration(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("name", "email", "password")