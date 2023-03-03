from django.urls import path
from . import views

urlpatterns = [
    path('api-token-auth/', views.CustomAuthToken.as_view()),
    path('company/', views.company_list),
    path('employee/<int:pk>/', views.employee_detail),
    path('device/', views.device_create),
    path('device/<int:pk>/', views.device_check_in),
]
