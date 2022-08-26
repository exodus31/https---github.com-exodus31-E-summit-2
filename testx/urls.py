from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('browse', views.browse, name="browse"),
    path('logout', views.logoutuser, name="logout"),
    path('signup', views.signup, name="signup"),
    path('signup_ent', views.signup_ent, name="signup_ent"),
    path('signup_inv', views.signup_inv, name="signup_inv"),
    path('createprof/<str:pk>', views.createprof, name="createprof"),
    path('login', views.login, name="login"), 
    path('yprofile/<str:pk>', views.yprofile, name="yprofile"),
    path('createprof/logout', views.logout, name="createproflogout"),
]