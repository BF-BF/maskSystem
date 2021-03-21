from django.contrib import admin
from django.urls import path
from searchCompare import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('mask_search', views.mask_search),
    path('keyword_search', views.keywords_search),
    path('compare', views.compare),
]