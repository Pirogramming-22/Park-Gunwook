from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('create/', views.idea_create, name='idea_create'),
    path('<int:idea_id>/', views.idea_detail, name='idea_detail'),
    path('<int:idea_id>/edit/', views.idea_edit, name='idea_edit'),
    path('<int:idea_id>/delete/', views.idea_delete, name='idea_delete'),
    path('update_like/<int:idea_id>/', views.update_like, name='update_like'),
    path('toggle_like/<int:idea_id>/', views.toggle_like, name='toggle_like'),
    path('update_like/<int:idea_id>/', views.update_like, name='update_like'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])