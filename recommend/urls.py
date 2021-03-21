from django.contrib import admin
from django.urls import path
from recommend import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('recommend', views.recommend),
]
