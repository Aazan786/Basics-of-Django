from django.contrib import admin
from .models import Reviews

# Register your models here.
class ReviewsAdmin(admin.ModelAdmin):
    list_display = ("user_name", "review_text", "rating")

admin.site.register(Reviews, ReviewsAdmin)