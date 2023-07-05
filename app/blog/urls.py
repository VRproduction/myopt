from django.urls import path
from blog.views import *


urlpatterns = [

    path('', index, name="index"),
    path('gallery', gallery, name="gallery"),
    path('about', about, name="about"),
    path('contact', contact, name="contact"),
    path('apointment', appointment, name="appointment"),

    path('services', services, name="services"),
    path('service_detail/<slug>', service_detail, name="service_detail"),

    path('blogs', blogs, name="blogs"),
    path('blog_detail/<slug>', blog_detail, name="blog_detail"),

    path('category_detail/<slug>', category_detail, name="category_detail"),
]






"""

urlpatterns = [

    path('', index, name="index"),
    path('gallery', gallery, name="gallery"),
    path('about', about, name="about"),
    path('contact/', contact, name="contact"),
    path('apointment', appointment, name="appointment"),

    path('services/', services, name="services"),
    path('service_detail/<slug>/', service_detail, name="service_detail"),

    path('blogs/', blogs, name="blogs"),
    path('blog_detail/<slug>/', blog_detail, name="blog_detail"),

    # path('asd/', asd, name="asd"),
    path('category_detail/<slug>/', category_detail, name="category_detail"),


]
"""

