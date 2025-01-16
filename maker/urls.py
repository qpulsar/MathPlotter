from django.urls import path
from pages.views import HomePageView
from .views import MakerView

urlpatterns = [
    path('maker/', MakerView.as_view(), name='maker'),  # Maker sayfası için URL
    # Diğer URL'ler...
] 