from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length = 255)
    
    class Meta:
        ordering = ("name",)#ordering by name
        verbose_name_plural = "Categories" #it gives the correct plural for category

    def __str__(self):
        return self.name #return the name as type in the admin objects
class Item(models.Model):
    category = models.ForeignKey(Category,on_delete = models.CASCADE,related_name = "itemsss")
    name = models.CharField(max_length = 255)
    description = models.TextField(blank = True,null = True)
    price = models.FloatField()
    image = models.ImageField(upload_to = "item_images",blank = True,null = True)
    is_sold = models.BooleanField(default = False)
    created_by = models.ForeignKey(User,related_name = "items",on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name