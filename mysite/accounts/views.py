from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, LoginForm


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
    return render(request, 'registration/profile.html', {'user': request.user})


# 홈 뷰
def home_view(request):
    return render(request, 'home.html')
# Create your views here.
