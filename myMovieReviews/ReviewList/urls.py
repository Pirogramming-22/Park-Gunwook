from django.urls import path
from . import views

urlpatterns = [
    path('', views.review_list, name='review_list'),  # 리뷰 리스트 페이지
    path('review/<int:pk>/', views.review_detail, name='review_detail'),  # 리뷰 디테일 페이지
    path('review/new/', views.review_create, name='review_create'),  # 새 리뷰 작성
    path('review/<int:pk>/edit/', views.review_edit, name='review_edit'),  # 리뷰 수정
    path('review/<int:pk>/delete/', views.review_delete, name='review_delete'),  # 리뷰 삭제
]