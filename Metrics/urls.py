from django.urls import path
from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("restaurant/<int:restaurant_id>", views.RestaurantDetailView.as_view(), name="Menu"),
    path("meal_reviews/<int:meal_id>", views.MealReviews.as_view(), name="MealReviews"),
    path('add_restaurant', views.AddRestaurant.as_view(), name="AddRestaurant"),
    path('add_meal', views.AddMeal.as_view(), name="AddMeal"),
    path('update_restaurant/<int:pk>', views.UpdateRestaurant.as_view(), name="UpdateRestaurant"),
    path('update_meal/<int:pk>', views.UpdateMeal.as_view(), name="UpdateMeal"),
    path('delete_meal/<int:pk>', views.DeleteMeal.as_view(), name="DeleteMeal"),
    path('delete_meal_reviews/<int:pk>', views.DeleteMealReviews.as_view(), name="DeleteMealReviews"),
    path('delete_restaurant/<int:pk>', views.DeleteRestaurant.as_view(), name="DeleteRestaurant"),
    path('delete_restaurant_reviews/<int:pk>', views.DeleteRestaurantReviews.as_view(), name="DeleteRestaurantReviews"),
    path('profile/<int:pk>', views.ProfileView.as_view(), name="ProfileView"),
    path('login/', views.LoginUser.as_view(), name="Login"),
    path('logout/', views.LogoutUser.as_view(), name="Logout"),
    path('register/', views.Register.as_view(), name="Register"),
    path('update_user/', views.UpdateUser.as_view(), name="UpdateUser"),



]
