from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/<int:_id>', views.otherprofile, name='otherprofile'),
    path('profile/edit', views.editprofile, name='editprofile'),
    path('profile/', views.profile, name='profile'),
]
