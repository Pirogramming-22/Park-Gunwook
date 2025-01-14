from django.urls import path
from . import views

urlpatterns = [
    path('', views.developtool_list, name='developtool_list'),
    path('create/', views.developtool_create, name='developtool_create'),
    path('<int:developtool_id>/', views.developtool_detail, name='developtool_detail'),
    
    path('<int:developtool_id>/edit/', views.developtool_edit, name='developtool_edit'),
    path('<int:developtool_id>/delete/', views.developtool_delete, name='developtool_delete'),
]
