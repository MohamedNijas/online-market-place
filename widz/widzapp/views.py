from django.shortcuts import render
from item.models import Category,Item
from .forms import SignupForm
# Create your views here.
def first_view(request):
    items = Item.objects.filter(is_sold = False)[:6]
    categories = Category.objects.all()
    context = {
        "categories":categories,
        "items":items
    }
    return render(request,"index.html",context)

def contact_view(request):
    return render(request,"contact.html")

def Signup(request):
    form = SignupForm()

    context = {
        "form":form
    }

    return render(request,"signupForm.html",context)
