from django.urls import path
from . import views
from .views import (
    case_list_view, case_create_view, case_update_view, 
    hearing_create_view, hearing_list_view, 
    hearing_index_view, hearing_detail_view, 
    hearing_update_view, case_add_hearing_view
)

urlpatterns = [
    path('', views.frontpage_view, name='index'),
    path('case/', case_list_view, name='case_list'),
    path('case/add/', case_create_view, name='case_create'),
    path('case/add_hearing/', case_add_hearing_view, name='case_add_hearing'),  # This line should be above
    path('case/<int:pk>/edit/', case_update_view, name='case_update'),
    path('case/<str:case_number>/', views.case_detail_view, name='case_detail'),
    path('case/<str:case_number>/hearings/', hearing_list_view, name='hearing_list'),
    path('case/<str:case_number>/hearing/add/', hearing_create_view, name='hearing_create'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('hearings/', hearing_index_view, name='hearing_index'),
    path('hearing/<int:pk>/', hearing_detail_view, name='hearing_detail'),
    path('hearing/<int:pk>/update/', hearing_update_view, name='hearing_update'),
    path('cases/judge/', views.case_list_judge_view, name='case_list_judge'),

]
