from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('register/', views.usr_reg_app, name='register'),
    path('login/', views.usr_log_app, name='login'),
    path('restorent_register/', views.rest_reg_app, name='restorent_register'),
    path('restorent_login/', views.rest_log_app, name='restorent_login'),
]
