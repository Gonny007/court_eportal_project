from django.urls import path
from . import views
from .views import case_list_view, case_create_view, case_update_view, hearing_create_view

urlpatterns = [
    path('', views.frontpage_view, name='index'),
    path('case/', case_list_view, name='case_list'),
    path('case/add/', case_create_view, name='case_create'),
    path('case/<int:pk>/edit/', case_update_view, name='case_update'),
    path('case/<str:case_number>/', views.case_detail, name='case_detail'),
    path('case/<str:case_number>/hearings/', views.hearing_list, name='hearing_list'),
    path('case/<int:case_pk>/hearings/add/', hearing_create_view, name='hearing_create'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('hearings/', views.hearing_index, name='hearing_index'),
    path('hearing/<int:pk>/', views.hearing_detail, name='hearing_detail'),  # Added URL pattern
    path('hearing/<int:pk>/update/', views.hearing_update, name='hearing_update'),  # Added URL pattern
    path('case/<str:case_number>/hearing/add/', views.hearing_create_view, name='hearing_create'),  # Added URL pattern

]
