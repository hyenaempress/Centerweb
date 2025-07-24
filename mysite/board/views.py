# board/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import JsonResponse
from .models import Post
from .forms import PostForm, GalleryPostForm

# 관리자 권한 확인 함수
def is_staff(user):
    return user.is_staff

# 일반 게시판 목록
def board_list(request):
    posts = Post.objects.filter(board_type='general').order_by('-created_at')
    paginator = Paginator(posts, 10)  # 페이지당 10개
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'board_list.html', {
        'posts': page_obj,
        'board_type': 'general'
    })

# 갤러리 목록
def gallery_list(request):
    posts = Post.objects.filter(board_type='gallery').order_by('-created_at')
    paginator = Paginator(posts, 9)  # 페이지당 9개
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'gallery.html', {
        'posts': page_obj,
        'board_type': 'gallery'
    })

# 관리자 게시판 목록
@user_passes_test(is_staff)
def admin_board_list(request):
    posts = Post.objects.filter(board_type='admin').order_by('-created_at')
    paginator = Paginator(posts, 10)  # 페이지당 10개
    
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'board/admin_board_list.html', {
        'posts': page_obj,
        'board_type': 'admin'
    })

# 게시글 상세보기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 조회수 증가 (작성자가 아닌 경우에만)
    if request.user != post.author:
        post.increment_views()
    
    return render(request, 'board/post_detail.html', {'post': post})

# 일반 게시글 작성
@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.board_type = 'general'
            post.save()
            messages.success(request, '게시글이 성공적으로 작성되었습니다.')
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'board/post_form.html', {
        'form': form,
        'title': '일반게시판 글 작성',
        'board_type': 'general'
    })

# 갤러리 게시글 작성
@login_required
def gallery_create(request):
    if request.method == 'POST':
        form = GalleryPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.board_type = 'gallery'
            post.save()
            messages.success(request, '갤러리 글이 성공적으로 업로드되었습니다.')
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = GalleryPostForm()
    
    return render(request, 'board/gallery_form.html', {
        'form': form,
        'title': '갤러리 글 작성',
        'board_type': 'gallery'
    })

# 관리자 게시글 작성
@login_required
@user_passes_test(is_staff)
def admin_post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.board_type = 'admin'
            post.save()
            messages.success(request, '관리자 게시글이 성공적으로 작성되었습니다.')
            return redirect('board:post_detail', pk=post.pk)
    else:
        form = PostForm()
    
    return render(request, 'board/post_form.html', {
        'form': form,
        'title': '관리자게시판 글 작성',
        'board_type': 'admin'
    })

# 게시글 수정 (작성자만)
@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자나 관리자만 수정 가능
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, '수정 권한이 없습니다.')
        return redirect('board:post_detail', pk=pk)
    
    if request.method == 'POST':
        if post.board_type == 'gallery':
            form = GalleryPostForm(request.POST, request.FILES, instance=post)
        else:
            form = PostForm(request.POST, instance=post)
            
        if form.is_valid():
            form.save()
            messages.success(request, '게시글이 성공적으로 수정되었습니다.')
            return redirect('board:post_detail', pk=pk)
    else:
        if post.board_type == 'gallery':
            form = GalleryPostForm(instance=post)
        else:
            form = PostForm(instance=post)
    
    template = 'board/gallery_form.html' if post.board_type == 'gallery' else 'board/post_form.html'
    
    return render(request, template, {
        'form': form,
        'post': post,
        'title': f'{post.get_board_type_display()} 글 수정',
        'board_type': post.board_type,
        'is_edit': True
    })

# 게시글 삭제 (작성자나 관리자만)
@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    
    # 작성자나 관리자만 삭제 가능
    if request.user != post.author and not request.user.is_staff:
        messages.error(request, '삭제 권한이 없습니다.')
        return redirect('board:post_detail', pk=pk)
    
    if request.method == 'POST':
        board_type = post.board_type
        post.delete()
        messages.success(request, '게시글이 삭제되었습니다.')
        
        # 게시판 타입에 따라 리다이렉트
        if board_type == 'gallery':
            return redirect('board:gallery_list')
        elif board_type == 'admin':
            return redirect('board:admin_board_list')
        else:
            return redirect('board:board_list')
    
    return render(request, 'board/post_confirm_delete.html', {'post': post})

# 좋아요 기능 (AJAX)
@login_required
def post_like(request, pk):
    if request.method == 'POST':
        post = get_object_or_404(Post, pk=pk)
        post.increment_likes()
        return JsonResponse({'likes': post.likes})
    return JsonResponse({'error': 'Invalid request'}, status=400)