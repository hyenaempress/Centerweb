# board/urls.py
from django.urls import path
from . import views

app_name = 'board'

urlpatterns = [
    # 게시판 목록
    path('', views.board_list, name='board_list'),
    path('gallery/', views.gallery_list, name='gallery_list'),
    path('admin/', views.admin_board_list, name='admin_board_list'),
    
    # 게시글 상세
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    
    # 게시글 작성
    path('create/', views.post_create, name='post_create'),
    path('gallery/create/', views.gallery_create, name='gallery_create'),
    path('admin/create/', views.admin_post_create, name='admin_post_create'),
    
    # 게시글 수정/삭제
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    
    # 좋아요
    path('post/<int:pk>/like/', views.post_like, name='post_like'),
]