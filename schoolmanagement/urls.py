"""schoolmanagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from rest_framework import routers
from myclass.views import studentViewset
from myclass import views
from django.contrib.auth import views as authentication_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


#for rest API
router = routers.DefaultRouter()
router.register('myclass',studentViewset)

urlpatterns = [
    path('admin/', admin.site.urls),

    #for rest API
    path('home/',include(router.urls)),
    path('index/', views.studentlist,name='studentlist'),

    #path  for user  login and logout 
    path('signup/', views.signup,name='signup'),
    path('',authentication_views.LoginView.as_view(template_name='myclass/login.html'),name='login'),
    path('logout/',views.logout,name='logout'),
    
    #creating path for Reset Password
    path('reset_password/', authentication_views.PasswordResetView.as_view(template_name='myclass/password_reset.html'),name='reset_password'),
    path('reset_password_sent/', authentication_views.PasswordResetDoneView.as_view(template_name='myclass/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', authentication_views.PasswordResetConfirmView.as_view(template_name='myclass/password_reset_form.html'), name='password_reset_confirm'),
    path('reset_password_complete/', authentication_views.PasswordResetCompleteView.as_view(template_name='myclass/password_reset_sent.html'), name='password_reset_complete'),

    #creating path for JWT Auth
    path('api/token/',TokenObtainPairView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),


]
