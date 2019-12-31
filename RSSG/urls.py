from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
	path('', views.home, name='RSSG-home'),
	path('alpha/', views.alpha, name='RSSG-alpha'),
    path('about/', views.about, name='RSSG-about'),
    path('gallery/', views.gallery, name='RSSG-gallery'),
    path('history/', views.history, name='RSSG-history'),
    path('operations/', views.operations, name='RSSG-operations'),
]