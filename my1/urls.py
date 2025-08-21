
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from my1 import settings
from . import views
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('register/',views.register),
    path('login/',views.login),
    path('contect/',views.contect),
    path('adminhome/',include('adminapp.urls')),
    path('studenthome/',include('studentapp.urls')),
    path('courselist1/',views.courselist1),
    path('batchlist1/',views.batchlist1),
    path('gallery/',views.gallery),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

