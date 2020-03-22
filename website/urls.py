from django.contrib import admin
from django.urls import path
from website.food.views import FoodView
from website import settings
from django.conf.urls.static import static


DEBUG = True

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FoodView.as_view(), name='main_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)