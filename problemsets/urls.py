from django.urls import path

from . import views

urlpatterns = [
    path('', views.problems, name='problems'),
    path('<int:_id>/', views.problemstmt),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
]
