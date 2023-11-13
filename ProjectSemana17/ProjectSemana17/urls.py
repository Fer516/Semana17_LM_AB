
from django.contrib import admin
from django.urls import path
from appsemana17.views import Lista

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Lista, name='lista'),
]
