"""
URL configuration for appsecrets project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysecret.urls')),
    path('signup/', user_views.register, name='sign_up'),
    path('signin/', auth_views.LoginView.as_view(template_name='users/login.html'), name='sign_in'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout_user'),
    path('home/', user_views.profile_home, name='profile_page'),
    path('profile/', user_views.profile_details, name='profile_details'),
    path('secrets/new/', user_views.new_secret, name='new_secret'),
    path('secrets/<str:sid>/', user_views.secret_details, name='secret_details'),
    path('secrets/<str:sid>/update/', user_views.secret_update, name='secret_update'),
    path('secrets/<str:sid>/delete/', user_views.confirm_secret_delete, name='confirm_secret_delete'),
    path('delete/<str:sid>/', user_views.delete_secret, name='delete_secret'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)