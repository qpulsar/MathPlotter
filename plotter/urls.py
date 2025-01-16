from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls'), name='home'),
    path('', include('maker.urls'), name='maker')
]
