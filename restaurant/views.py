from django.shortcuts import get_object_or_404, render
from .models import Foods, Category, Review
from .forms import ReviewForm

def menu(request):
    categories = Category.objects.all()
    foods = Foods.objects.all()
    
    # محاسبه میانگین با پایتون ساده برای تک تک غذاها در منو
    for food in foods:
        reviews = Review.objects.filter(food=food, status='approved')
        
        total_score = 0
        count = 0
        
        # یک حلقه ساده برای جمع زدن امتیازات
        for review in reviews:
            total_score += review.rating
            count += 1
            
        # محاسبه میانگین (جلوگیری از خطای تقسیم بر صفر)
        if count > 0:
            food.calculated_avg = total_score / count
        else:
            food.calculated_avg = 0  # امتیاز پیش‌فرض اگر نظری نبود

    return render(request, 'restaurant/menu.html', context={"foods": foods, "categories": categories})


def food_detail_view(request, pk):
    food = get_object_or_404(Foods, pk=pk)
    reviews = Review.objects.filter(food=food, status='approved')
    
    # محاسبه میانگین با پایتون ساده برای همین یک غذا
    total_score = 0
    count = 0
    for review in reviews:
        total_score += review.rating
        count += 1
        
    if count > 0:
        food.calculated_avg = total_score / count
    else:
        food.calculated_avg = 0

    # بخش ثبت نظر جدید
    if request.method == 'POST':
        comment = ReviewForm(request.POST)
        if comment.is_valid():
            new_comment = comment.save(commit=False)
            new_comment.food = food
            new_comment.status = 'pending'
            new_comment.save()
            comment = ReviewForm()
    else:
        comment = ReviewForm()
        
    return render(request, "restaurant/food_detail.html", context={
        'food': food, 
        'form': comment, 
        'reviews': reviews
    })
