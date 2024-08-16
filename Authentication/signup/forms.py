from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class Signup(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class UserEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
        labels = {"email": "Email"}

class AdminEditForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = "__all__"
        labels = {"email": "Email"}
