from django.urls import path

from users import views

app_name = 'users'

urlpatterns = [
    path('login/', views.login),
    path('login/<int:id>/', views.login_detail, name='login-detail'),
]
