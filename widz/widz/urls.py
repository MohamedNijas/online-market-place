from django.contrib import admin #imported for admin
from django.conf import settings#imported for image
from django.conf.urls.static import static #imported for image
from django.urls import path,include
from widzapp.views import first_view,contact_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",include("widzapp.urls")),
    path("items/",include("item.urls")),#if the url start with item ulrss
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
