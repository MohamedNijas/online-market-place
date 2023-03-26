from django.contrib import admin
from .models import Category,Item
# Register your models here.
admin.site.register(Category)#register the category inside the admin to see the  category in the admin 
admin.site.register(Item)