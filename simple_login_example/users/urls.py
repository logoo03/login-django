from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('login/<str:id>/', views.login_detail, name='login-detail'),
    path('logout/', views.logout, name='logout'),
    path('login/index', views.index, name='index'),
    path('register/', views.register, name='register')
]
