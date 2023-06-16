from django.contrib import admin
from .models import Meal, ReviewMeal, ReviewRestaurant, Restaurant, Profile
from django.contrib.auth.models import User

admin.site.register(Meal)
admin.site.register(ReviewMeal)
admin.site.register(ReviewRestaurant)
admin.site.register(Restaurant)


class ProfileInLine(admin.StackedInline):
    model = Profile


class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [ProfileInLine]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
