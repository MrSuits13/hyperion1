# hyperion1/urls.py

from django.contrib import admin
from django.urls import include, path
from user_auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('user_auth/', include("user_auth.urls")),
]
