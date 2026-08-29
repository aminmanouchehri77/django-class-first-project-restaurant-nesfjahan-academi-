
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Foods,Category,Review
from .forms import ReviewForm

def menu(request):
    categories=Category.objects.all()
    foods=Foods.objects.all()
    return render(request,'restaurant/menu.html',context={"foods":foods,"categories":categories})



def food_detail_view(request,pk):
    food=get_object_or_404(Foods,pk=pk)
    reviews=Review.objects.filter(food=food,status='approved')
    if request.method=='POST':
        comment=ReviewForm(request.POST)
        if comment.is_valid():
            new_comment=comment.save(commit=False)
            new_comment.food=food
            new_comment.status=Review.STATUS_CHOICES[0]
            new_comment.save()
            comment=ReviewForm()
    else:
        comment=ReviewForm()
        
    return render(request,"restaurant/food_detail.html",context={'food':food,'form':comment,'reviews':reviews})