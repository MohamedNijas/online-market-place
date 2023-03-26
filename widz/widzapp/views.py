from django.shortcuts import render,redirect
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
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect("/login/")

    else:
        form = SignupForm()
    context = {
        "form":form
    }
    return render(request,"signup.html",context)
