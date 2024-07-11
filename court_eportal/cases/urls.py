from django.urls import path
from . import views

urlpatterns = [
    path('', views.frontpage_view, name='frontpage_view'),
    path('case/', views.case_list, name='case_list'),
    path('case/<str:case_number>/', views.case_detail, name='case_detail'),
    path('case/<str:case_number>/hearings/', views.hearing_list, name='hearing_list'),
]
