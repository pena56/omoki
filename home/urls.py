from django.urls import path

from . import views

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('services/', views.service_page_view, name='service'),
    path('services/<int:id>',views.category_detail_view, name='category_detail'),
    path('gallery/', views.gallery_view, name='gallery'),
    path('gallery/<int:id>', views.event_view, name='event_detail'),
    path('team/', views.team_view, name='team'),
    path('contact/',views.contact_view, name='contact'),
    path('success/', views.contact_success_view, name='success'),
]