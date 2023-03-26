from django.contrib.auth import views as auth_views

from django.urls import path
from .views import first_view,contact_view,Signup
from .forms import LoginForm
app_name = "widzapp"

urlpatterns = [
    path('',first_view,name = "index"),
    path("contact/",contact_view,name = "contact"),
    path("Signup/",Signup,name = "signup"),
    path("login/",auth_views.LoginView.as_view(authentication_form = LoginForm),name = "login"),
]