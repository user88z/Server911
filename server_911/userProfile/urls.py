from django.urls import path
from .views import view_profile, Device_parametrs
from django.contrib.auth import views

urlpatterns = [
     path('', view_profile, name='device_profile'),
     path('login/', views.LoginView.as_view(template_name='registration/login.html'), name='login'),
     path('logout/', views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
     path('<imei>/', Device_parametrs.as_view(), name='device_detail'),
 ]
