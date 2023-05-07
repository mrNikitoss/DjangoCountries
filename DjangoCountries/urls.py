from django.contrib import admin
from django.urls import path
from MainApp import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('countries_list/', views.countries_list),
    path('country/<int:id>/', views.country_page),
    path('languages/', views.languages),

]