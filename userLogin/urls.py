from django.contrib import admin
from django.urls import path
from userLogin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('userLogin', views.signin),
    path('register', views.register),
]
