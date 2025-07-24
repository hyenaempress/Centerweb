from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm, ProfileForm
from .models import Profile


# 회원가입 뷰
def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'{username}님, 회원가입이 완료되었습니다!')
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '회원가입 중 오류가 발생했습니다.')
    else:
        form = SignUpForm()

    return render(request, 'registration/signup.html', {'form': form})


# 로그인 뷰
def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'{username}님, 환영합니다!')
                return redirect('home')
        else:
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})


# 로그아웃 뷰
@login_required
def logout_view(request):
    username = request.user.username
    logout(request)
    messages.success(request, f'{username}님, 로그아웃되었습니다.')
    return redirect('home')


# 프로필 뷰
@login_required
def profile_view(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, '프로필이 업데이트되었습니다.')
            return redirect('accounts:profile')
        else:
            messages.error(request, '프로필 업데이트 중 오류가 발생했습니다.')
    else:
        form = ProfileForm(instance=profile)
    
    return render(request, 'registration/profile.html', {
        'user': request.user,
        'profile': profile,
        'form': form
    })


# 홈 뷰
def home_view(request):
    from board.models import Post
    
    # 각 게시판별 최신글 3개씩 가져오기
    general_posts = Post.objects.filter(board_type='general').order_by('-created_at')[:3]
    gallery_posts = Post.objects.filter(board_type='gallery').order_by('-created_at')[:3]
    admin_posts = Post.objects.filter(board_type='admin').order_by('-created_at')[:3]
    
    context = {
        'general_posts': general_posts,
        'gallery_posts': gallery_posts,
        'admin_posts': admin_posts,
    }
    
    return render(request, 'home.html', context)

# 갤러리 뷰 (임시)
def gallery_view(request):
    return render(request, 'gallery.html')

# 게시판 리스트 뷰 (임시)
def board_list_view(request):
    return render(request, 'board_list.html')

# 게시판 상세 뷰 (임시)
def board_detail_view(request):
    return render(request, 'board_detail.html')

# 게시판 작성 뷰 (임시)
def board_write_view(request):
    return render(request, 'board_write.html')

# 갤러리 상세 뷰 (임시)
def gallery_detail_view(request):
    return render(request, 'gallery_detail.html')

# 갤러리 작성 뷰 (임시)
def gallery_write_view(request):
    return render(request, 'gallery_write.html')
# Create your views here.
