from django.urls import path

from .views import first_view,contact_view

app_name = "widzapp"

urlpatterns = [
    path('',first_view,name = "index"),
    path("contact/",contact_view,name = "contact")
]