from django.urls import path

from . import views

#app_name = 'encyc'

urlpatterns = [
    path("", views.index, name="index"),
    path('create', views.create, name='create'),
    path("<str:title>", views.title, name='title'),
    path("<str:title>/edit", views.edit, name='edit'),
    path('random/', views.random_page, name='random'),
    path('search', views.search, name='search')





]
