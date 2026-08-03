import uuid
from django.db import models

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
 
 
    