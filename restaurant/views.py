
from django.http import HttpResponse
from django.shortcuts import render
from .models import Foods,Category

def menu(request):
    categories=Category.objects.all()
    foods=Foods.objects.all()
    return render(request,'restaurant/menu.html',context={"foods":foods,"categories":categories})



def food_detail(request,pk):
    food=Foods.objects.filter(pk=pk)