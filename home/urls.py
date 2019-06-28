from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('s/', views.service_page_view, name='service'),
]