# urls.py
from django.urls import path
from . import views

app_name = 'instagram'

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('post/<int:post_id>/like/', views.toggle_like, name='toggle_like'),  # 좋아요 처리 경로
    path('post/<int:post_id>/add-comment/', views.add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', views.delete_comment, name='delete_comment'),
]
