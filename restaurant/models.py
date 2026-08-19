import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
class Category(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    title=models.CharField(max_length=100)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
            return(f'{self.title}')
        
    
    
class Foods(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name=models.CharField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.PROTECT,related_name='foods')
    # فیلد عکس غذا
    image = models.ImageField(
        upload_to='foods/',
        blank=True,
        null=True,
        verbose_name='تصویر غذا'
    )
    price=models.PositiveIntegerField()
    content=models.TextField()
    is_exist=models.BooleanField()
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f'{self.name}')
 
 
class Review(models.Model):
    # تعریف حالت‌های مختلف وضعیت
    STATUS_CHOICES = [
        ('pending', 'در انتظار تایید'),
        ('approved', 'تایید شده'),
        ('rejected', 'رد شده'),
    ]

    food = models.ForeignKey(
        'Foods', 
        on_delete=models.CASCADE, 
        related_name='reviews', 
        verbose_name='غذا'
    )
    
    name = models.CharField(max_length=100, verbose_name='نام کاربر')
    comment = models.TextField(verbose_name='متن نظر')
    
    rating = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(5)],
        verbose_name='امتیاز'
    )
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ثبت')
    
    # تغییر فیلد قبلی به فیلد وضعیت با سه حالت
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending',
        verbose_name='وضعیت نمایش'
    )

    class Meta:
        verbose_name = 'نظر'
        verbose_name_plural = 'نظرات'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.food.name} ({self.get_status_display()})"

    # یک متد کمکی برای نمایش ستاره‌ها در قالب
    def get_stars_range(self):
        return range(self.rating)
    