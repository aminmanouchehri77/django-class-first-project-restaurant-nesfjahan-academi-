
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Foods,Category


def menu(request):
    categories=Category.objects.all()
    foods=Foods.objects.all()
    return render(request,'restaurant/menu.html',context={"foods":foods,"categories":categories})



def food_detail_view(request,pk):
    food=get_object_or_404(Foods,pk=pk)
    return render(request,"restaurant/food_detail.html",context={'food':food})