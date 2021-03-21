from django.contrib import admin
from django.urls import path
from searchCompare import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('maskSearch', views.mask_search),
    path('keywordSearch', views.keywords_search),
    path('compare', views.compare),
]