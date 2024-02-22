# personal/urls.py
from django.urls import path
from .views import about_me
from .views import home_page
from .views import contact_page 

urlpatterns = [
    path('about/', about_me, name='about_me'),
    path('home/', home_page, name='home.html' ),
    path('contact/', contact_page, name='contact.html' )
]
