
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('HomePageApp.urls'), name='home'),
    path('Account/', include('usr_account.urls'), name='Account')
]
