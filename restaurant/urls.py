
from django.urls import path
from . import views



urlpatterns = [
    path("",views.menu,name="menu"),
    path('food/<int:pk>',views.food_detail,name="food_detail")
    
]

