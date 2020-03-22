from django.contrib import admin
from django.urls import path
from website.food.views import FoodView, signup, DeleteFood
from website import settings
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url, include
from django.contrib.auth import views as auth_views


DEBUG = True

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FoodView.as_view(), name='main_page'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', auth_views.LoginView, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.LogoutView, {'next_page': 'main_page'}, name='logout'),
]

urlpatterns += staticfiles_urlpatterns()

# if settings.DEBUG:
    # urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)