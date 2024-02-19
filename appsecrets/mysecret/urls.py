from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('profile/', views.profile_home, name='profile_page'),
    path('about/', views.about_page, name='about_page'),
    path('contact/', views.contact_page, name='contact_page'),
    path('signin/', views.signin_user, name='sign_in'),
    path('signup/', views.signup_user, name='sign_up'),

]
