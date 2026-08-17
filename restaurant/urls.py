
from django.urls import path
from . import views



urlpatterns = [
    path("",views.menu,name="menu"),
    path('food/<uuid:pk>',views.food_detail_view,name="food_detail")
    
]

