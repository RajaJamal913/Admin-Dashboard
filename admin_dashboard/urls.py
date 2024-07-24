# admin_dashboard/urls.py
from django.urls import path
from . import views

app_name = 'admin_dashboard'

urlpatterns = [
    path('', views.overview, name='overview'),
    path('user_list/', views.user_list, name='users'),
    path('order_list/', views.order_list, name='orders'),
      path('ip_banning/', views.ip_banning, name='ip_banning'),
      path('activity_logs/', views.activity_logs, name='activity_logs'),
      path('staff_list/', views.staff_list, name='staff_list'),
       path('api_management/', views.api_management, name='api_management'),
    path('api_management/toggle/<int:api_id>/', views.toggle_api_status, name='toggle_api_status'),
    path('api_management/delete/<int:api_id>/', views.delete_api, name='delete_api'),
    path('api_management/add/', views.add_duplicate_api, name='add_duplicate_api'),
   path('panel-rate-management/', views.panel_rate_management, name='panel_rate_management'),
    path('order-panel-configuration/', views.order_panel_configuration, name='order_panel_configuration'),
    # Add more paths as needed
]
