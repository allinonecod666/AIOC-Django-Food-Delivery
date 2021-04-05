from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.LandingPage, name='LandingPage'),
    path('/<restname>', views.RestorentDetailsFun, name='RestorentDetails')
]
