from django.contrib import admin
from django.urls import path,include
from calc import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('calc.urls')),
]
