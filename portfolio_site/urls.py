from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home & About
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),

    # Apps
    path('projects/', include('projects_app.urls')),
    path('contact/', include('contact_app.urls')),
    path('', include('accounts_app.urls')),   
    path('api/', include('api_app.urls')),

    # Authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

# Media files
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)