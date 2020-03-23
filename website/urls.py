from django.contrib import admin
from django.urls import path, include
from website.food.views import FoodView, DeleteFood
from website import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from django.contrib.auth import views as auth_views


DEBUG = True

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', FoodView.as_view(), name='main_page'),
#     ]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), 
    path('', FoodView.as_view(), name='main_page'),
    ]

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)