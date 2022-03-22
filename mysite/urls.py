from django.contrib import admin
from django.urls import include, path
from rest_framework import routers                 
from myapp import views

router = routers.DefaultRouter()                   
router.register(r'contact', views.ContactView, 'contact')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
