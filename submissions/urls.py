from django.urls import path

from . import views

urlpatterns = [
    path('', views.submissions, name='submissions'),
    path('<int:_id>/', views.submissiondetails),
    # path('logout/', views.logout, name='logout'),
    # path('register/', views.register, name='register'),
]
