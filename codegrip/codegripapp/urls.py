from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('api/deleteemployee/', views.DeletemployeeAPI.as_view()),
    path('api/editemployee/', views.EditemployeeAPI.as_view()),
    path('api/getemployee/', views.GetemployeeAPI.as_view()),
    path('api/addemployee/', views.AddemployeeAPI.as_view()),
    path('api/signup/', views.SignupAPI.as_view()),
    path('api/login/', views.LoginAPI.as_view()),
    path('', views.Home.as_view()),
]
