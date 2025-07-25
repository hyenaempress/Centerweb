# CenterWeb - Django 게시판 시스템

> Django 기반의 웹 게시판 시스템 개발 프로젝트  
> **🎯 목표 개발 일정**: 2024년 7월 25일 (과제 마감일)

## 📋 프로젝트 개요

Master Board라는 이름의 다기능 게시판 시스템으로, 일반게시판, 갤러리, 관리자게시판으로 구성된 웹 애플리케이션입니다.

## 👥 팀 구성 및 역할

- **박수연**: 프로젝트 매니저(PM), 개발 리드, 일정관리, 산출물 양식 제공, 템플릿 개발, 모듈 통합, 리빌드 총괄
- **진범광**: 로그인/로그아웃 시스템, 프론트엔드 HTML 개발
- **박태응**: 게시판 시스템

## 📅 개발 일정

### 7월 14일 (월) - 기획 단계
- **화면 기획서 생성**
- 📄 [화면 기획서](https://docs.google.com/presentation/d/1HXLl8taSYfnHUcu97CE_e_38ZJsg5f--9Y8p7ejvA50/edit?slide=id.g36f0db1316f_0_14#slide=id.g36f0db1316f_0_14)
- ⚠️ *전체 오픈 전에 문서 권한을 수정 금지로 변경 필요*

### 7월 15일 (화) - 공통 작업
- **박수연**: 템플릿 가이드 작업
- **진범광**: 로그인/로그아웃 시스템
- **박태응**: 게시판 시스템

### 7월 17일 (목) - 설계 단계
- **정보구조도 작성** (API, 모듈 메소드 정의)
- **공통 작업**: 박수연(템플릿), 진범광(로그인/로그아웃), 박태응(게시판)
- 📊 [정보구조도](https://docs.google.com/spreadsheets/d/1fUmVRob5ohQaRx0xdFUBkKXlmy8_MypxEYe9jBGj3RY/edit?gid=0#gid=0)

### 7월 18일 (금) ~ 7월 21일 (월) - DB 설계
- **ERD 테이블 설계**
- **참여자**: 박수연, 진범광, 박태응

### 7월 22일 (화) - 시스템 설계
- **Django 기반 개발 협의**
- **시퀀스 다이어그램 설계**
- 🔄 [시퀀스 다이어그램](https://docs.google.com/presentation/d/1FdBdHsF7lQUe7RR2OwpxSbOEGs4T7JsmxRKOQMq6QSg/edit)
- **공통 작업**: 박수연(템플릿), 진범광(로그인/로그아웃), 박태응(게시판)

### 7월 23일 (수) - 개발 시작
- **Django 기반 개발 시작**
- **시퀀스 다이어그램 기반 모듈 개발**
- **개발자**: 진범광(로그인/로그아웃), 박태응(게시판)
- **프론트엔드 HTML 개발**: 진범광 (전체 HTML 템플릿 작업) - https://github.com/JinBeomKwang/-html-
- ✅ **모듈 테스트 완료**
- ❌ **문제 발생**: 모듈 연계 과정에서 Django ORM과 MariaDB 데이터 USER 베이스 쿼리 충돌 문제
- **디버깅 담당**: 박수연, 박태응, 진범광

### 7월 24일 (목) - 리빌드
- **HTML 템플릿 전달**: 진범광 → 박수연 (목요일까지 작업 완료)
- **전체 모듈 통합**: 박수연이 모든 모듈을 받아서 통합 작업
- **ORM 기반 리빌드 결정**
- **Django 라이브러리 기반으로 회원 모듈 변경**
- **어드민 APP, BOARD APP 분할**
- **순차 모듈 결합 작업**: 박수연 (리빌드 총괄)

1. 회원가입/로그인 (기반 시스템)
2. User 모델 + 프로필 (데이터 모델)
3. HTML 디자인 통합 (프레젠테이션 레이어)
4. 보드 앱 생성 (모듈 분리)
5. 게시판 → 갤러리 (핵심 비즈니스 로직)
6. 삭제/업로드 (세부 기능)
7. 경로 수정 (라우팅)
8. 어드민 페이지 (관리 기능)
  
✅ 1층: 인증 시스템 (Foundation)
✅ 2층: 데이터 모델 (Data Layer)  
✅ 3층: UI 통합 (Presentation Layer)
✅ 4층: 비즈니스 로직 (Business Layer)
✅ 5층: 관리 기능 (Admin Layer)

1차 개발 완료 

### 7월 25일 (금) - 통합 테스트 및 과제 완료
- **🎯 과제 마감일**
- **통합 테스트 QA**
- **프리테스트 기반 QA 요청 문서 작성**
- **QA**: 진범광(로그인/로그아웃), 박태응(게시판)
- **개발 완료**: 목표 일정 내 성공적 완료 ✅

- 📋 [QA 요청 문서](https://docs.google.com/presentation/d/15l9z946mHTCSn7FTQYzodXyT3QAiSB1OdqPsf2xuq0k/edit)

- ### 7월 25일 (금) - 과제 외 추가진행
- **배포 작업**: 박수연이 Google Cloud App Engine 배포 진행 (완료)
- **운영 환경 구축**: 파일 업로드, DB 이슈 해결 및 실서비스 배포 (완료)
- **반응형 업데이트**: 진범광, 반응형 CSS 적용 (진행중/적용전)

## 🛠 기술 스택

### Backend Framework
- **Django 5.2.4** - Python 웹 프레임워크
- **Python 3.13.5** - 프로그래밍 언어

### Database
- **SQLite 3.49.1** - 개발환경 데이터베이스
- **Django ORM** - 객체 관계 매핑

### Frontend
- **HTML5** - 마크업 언어
- **CSS3** - 스타일시트
- **JavaScript (ES6+)** - 클라이언트 사이드 스크립팅
- **Responsive Design** - 반응형 웹 디자인

### Authentication & Security
- **Django Authentication System** - 내장 인증 시스템
- **CSRF Protection** - Cross-Site Request Forgery 방어
- **User Permission System** - 사용자 권한 관리

### Development Environment
- **Windows 11** - 개발 운영체제
- **Git** - 버전 관리 시스템
- **Virtual Environment** - Python 가상환경

### Additional Libraries
- **Pillow** - 이미지 처리 라이브러리
- **Django Static Files** - 정적 파일 관리
- **Django Media Files** - 미디어 파일 관리

## 📁 프로젝트 구조

```
Centerweb/
├── mysite/                 # Django 프로젝트 설정
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py         # 프로젝트 설정
│   ├── urls.py             # 메인 URL 라우팅
│   └── wsgi.py
├── accounts/               # 사용자 인증 앱
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py           # 회원가입/로그인 폼
│   ├── models.py          # 사용자 모델 확장
│   ├── tests.py
│   ├── urls.py            # 인증 관련 URL
│   └── views.py           # 로그인/로그아웃/회원가입 뷰
├── board/                  # 게시판 앱
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py           # 게시글 작성 폼
│   ├── models.py          # 게시글 모델
│   ├── tests.py
│   ├── urls.py            # 게시판 URL
│   └── views.py           # 게시판 뷰 로직
├── media/                  # 업로드 파일 저장소
├── templates/              # HTML 템플릿
│   ├── board/             # 게시판 템플릿
│   │   ├── admin_board_list.html  # 관리자 게시판 목록
│   │   ├── gallery_form.html      # 갤러리 작성 폼
│   │   ├── post_confirm_delete.html # 게시글 삭제 확인
│   │   ├── post_detail.html       # 게시글 상세 보기
│   │   └── post_form.html         # 게시글 작성 폼
│   ├── registration/      # 인증 템플릿
│   │   ├── login.html     # 로그인 페이지
│   │   ├── profile.html   # 프로필 페이지
│   │   └── signup.html    # 회원가입 페이지
│   ├── base.html          # 기본 템플릿
│   ├── board_detail.html  # 게시글 상세
│   ├── board_list.html    # 게시판 목록
│   ├── board_write.html   # 게시글 작성
│   ├── gallery.html       # 갤러리 목록
│   ├── gallery_detail.html# 갤러리 상세
│   ├── gallery_write.html # 갤러리 작성
│   └── home.html          # 메인 홈페이지
├── db.sqlite3             # SQLite 데이터베이스
├── manage.py              # Django 관리 명령어
└── README.md              # 프로젝트 문서
```

## 🎯 주요 기능

### 사용자 인증 시스템
- ✅ **회원가입** - 사용자 등록 및 프로필 생성
- ✅ **로그인/로그아웃** - 세션 기반 인증
- ✅ **프로필 관리** - 개인정보 수정 및 프로필 이미지 업로드
- ✅ **권한 관리** - 일반사용자/관리자 권한 분리
- ✅ **보안 기능** - CSRF 토큰, 비밀번호 해싱

### 게시판 시스템
- ✅ **일반게시판** - 로그인 사용자 전용 텍스트 게시판
- ✅ **갤러리** - 이미지 업로드 및 미리보기 지원
- ✅ **관리자게시판** - 스태프 권한 필요한 공지사항 게시판
- ✅ **CRUD 기능** - 게시글 생성, 조회, 수정, 삭제
- ✅ **조회수/좋아요** - 게시글 조회수 증가 및 좋아요 기능
- ✅ **페이징 처리** - 대용량 데이터 효율적 표시
- ✅ **검색 및 필터링** - 게시판별 콘텐츠 분류

### 홈페이지 대시보드
- ✅ **최신글 미리보기** - 각 게시판별 최신 게시글 3개씩 표시
- ✅ **통합 네비게이션** - 일관된 사용자 경험

### 관리 기능
- ✅ **Django Admin** - 관리자 페이지 통합
- ✅ **사용자 관리** - 회원 정보 및 권한 관리
- ✅ **콘텐츠 관리** - 게시글 및 이미지 관리
- ✅ **데이터베이스 관리** - ORM 기반 데이터 조작

## 🔧 설치 및 실행

### 시스템 요구사항
- **Python**: 3.13.5 이상
- **Django**: 5.2.4 이상
- **OS**: Windows 11 (개발환경 기준)

### 설치 가이드

```bash
# 1. 프로젝트 클론
git clone [repository-url]
cd CenterWeb/mysite

# 2. 가상환경 생성 및 활성화
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/macOS
source venv/bin/activate

# 3. 필수 의존성 설치
pip install django==5.2.4
pip install pillow  # 이미지 처리용

# 4. 데이터베이스 설정
python manage.py makemigrations accounts
python manage.py makemigrations board
python manage.py migrate

# 5. 슈퍼유저 생성 (관리자 계정)
python manage.py createsuperuser
# Username: admin
# Password: admin123 (예시)

# 6. 개발 서버 실행
python manage.py runserver
```

### 기본 계정 정보
- **관리자 계정**: `admin` / `admin123`
- **접속 URL**: `http://127.0.0.1:8000/`
- **관리자 페이지**: `http://127.0.0.1:8000/admin/`

### 디렉토리 구조 확인
```bash
# 프로젝트 구조 확인
cd CenterWeb
tree /F  # Windows
# 또는
find . -type f | head -20  # Linux/macOS
```

## 🚀 주요 해결 과제

### 1. Django ORM과 MariaDB 충돌 문제
- **문제**: 사용자 테이블 쿼리 충돌
- **해결**: Django 기본 ORM으로 전환, SQLite 사용

### 2. 모듈 분리 및 통합 과정
- **프로젝트 관리**: 박수연의 PM 역할로 일정관리 및 개발 리드
- **표준화**: 산출물 양식 제공으로 팀 작업 효율성 향상
- **개발 분담**: 각자 담당 모듈 개발
- **HTML 템플릿**: 진범광이 전체 프론트엔드 담당
- **모듈 통합**: 박수연이 모든 모듈을 받아서 통합
- **리빌드 결정**: ORM 충돌 문제로 인한 전면 재구성
- **accounts 앱**: 사용자 인증 전담
- **board 앱**: 게시판 기능 전담
- **관심사의 분리**로 유지보수성 향상

### 3. 권한 관리 시스템
- **일반 사용자**: 일반게시판, 갤러리 작성 가능
- **관리자**: 모든 게시판 작성 및 관리 가능

## 📝 문서 링크

- [화면 기획서](https://docs.google.com/presentation/d/1HXLl8taSYfnHUcu97CE_e_38ZJsg5f--9Y8p7ejvA50/edit?slide=id.g36f0db1316f_0_14#slide=id.g36f0db1316f_0_14)
- [정보구조도](https://docs.google.com/spreadsheets/d/1fUmVRob5ohQaRx0xdFUBkKXlmy8_MypxEYe9jBGj3RY/edit?gid=0#gid=0)
- [시퀀스 다이어그램](https://docs.google.com/presentation/d/1FdBdHsF7lQUe7RR2OwpxSbOEGs4T7JsmxRKOQMq6QSg/edit)
- [QA 요청 문서](https://docs.google.com/presentation/d/15l9z946mHTCSn7FTQYzodXyT3QAiSB1OdqPsf2xuq0k/edit)

## 🎉 프로젝트 성과

- ✅ **목표 일정 내 성공적 완료**: 7월 25일 과제 마감일 준수
- ✅ **체계적인 프로젝트 관리**:  PM 역할로 효율적 일정/프로세스 관리
- ✅ **표준화된 개발 프로세스**: 산출물 양식 제공으로 일관된 문서화
- ✅ **시퀀스 다이어그램 기반 체계적 개발**
- ✅ **Django 표준 아키텍처 적용**
- ✅ **모듈별 역할 분담을 통한 효율적 협업**
- ✅ **문제 해결 과정에서 기술적 성장**
- ✅ **개발 통합 관리로 성공적 프로젝트 완료**

## 🌐 배포 (Google App Engine) 
브런치 gc_server
현재 배포 중지, 계정 폐쇄 

### 배포된 사이트
- **Production URL**: https://centerweb-project.du.r.appspot.com
- **관리자 계정**: `admin` / `변경되었음, 비공개`
- **배포 플랫폼**: Google Cloud App Engine
- **배포 일시**: 2025년 7월 25일

### 배포 환경 설정

#### 필요 파일
```
Centerweb/
├── app.yaml              # App Engine 설정 파일
├── main.py               # WSGI 애플리케이션 진입점
├── requirements.txt      # Python 의존성
└── .gcloudignore        # 배포 제외 파일 설정
```

#### app.yaml 설정
```yaml
runtime: python311

env_variables:
  SECRET_KEY: "django-insecure-your-secret-key"
  DEBUG: "False"

handlers:
- url: /static
  static_dir: staticfiles
- url: /.*
  script: auto

automatic_scaling:
  min_instances: 1
  max_instances: 3
  target_cpu_utilization: 0.6
```

#### main.py (WSGI 진입점)
```python
import os
import sys
from django.core.wsgi import get_wsgi_application

# Django 프로젝트 경로 추가
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mysite'))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')

# 자동 데이터베이스 마이그레이션 및 관리자 계정 생성
try:
    import django
    django.setup()
    from django.core.management import call_command
    from django.contrib.auth.models import User
    
    call_command('migrate', verbosity=0, interactive=False)
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        
except Exception as e:
    print(f"Setup error: {e}")

app = get_wsgi_application()
```

#### requirements.txt
```
Django==5.2.4
Pillow==11.3.0
gunicorn==21.2.0
```

### 배포 과정

#### 1. 사전 준비
```bash
# Google Cloud SDK 설치 후
gcloud init
gcloud auth login
gcloud config set project centerweb-project
```

#### 2. 배포 설정
```bash
cd D:\Centerweb

# 정적 파일 수집
cd mysite
python manage.py collectstatic --noinput
cd ..

# 배포 실행
gcloud app deploy
```

#### 3. 배포 후 확인
```bash
# 애플리케이션 열기
gcloud app browse

# 로그 확인
gcloud app logs tail -s default
```

### 배포 환경 특징

#### 데이터베이스 설정
- **로컬 환경**: SQLite (`db.sqlite3`)
- **App Engine 환경**: 임시 SQLite (`/tmp/db.sqlite3`)
- **자동 마이그레이션**: 앱 시작 시 자동 실행
- **관리자 계정**: 자동 생성 (`admin` / `admin123`)

#### 주요 해결 과제
1. **읽기 전용 파일시스템 문제**
   - App Engine의 읽기 전용 환경
   - `/tmp` 디렉토리 활용으로 해결

2. **정적 파일 처리**
   - `STATIC_ROOT = 'staticfiles'` 설정
   - `collectstatic` 명령어로 수집

3. **환경별 설정 분리**
   - `GAE_APPLICATION` 환경변수로 운영/개발 구분
   - `DEBUG` 모드 환경변수 제어

### 모니터링 및 관리

```bash
# 버전 관리
gcloud app versions list

# 트래픽 분할
gcloud app services set-traffic default --splits=VERSION_ID=1

# 로그 모니터링
gcloud app logs tail -s default --level=info
```

### 배포 체크리스트
- [x] `app.yaml` 파일 생성
- [x] `main.py` WSGI 앱 설정
- [x] `requirements.txt` 의존성 정의
- [x] `settings.py` ALLOWED_HOSTS 설정
- [x] 정적 파일 수집 (`collectstatic`)
- [x] 데이터베이스 환경별 설정
- [x] 자동 마이그레이션 설정
- [x] 관리자 계정 자동 생성
- [x] 배포 및 동작 확인

## 🐛 배포 중 발견된 주요 이슈 및 해결방법

### 2025년 7월 25일 추가 디버깅 과정

#### 1. 갤러리 이미지 업로드 실패 문제

**문제 상황**:
```
OSError: [Errno 30] Read-only file system: '/workspace/gallery'
```

**원인 분석**:
- App Engine 환경의 읽기 전용 파일시스템 제약
- Django가 Google Cloud Storage 대신 로컬 파일시스템 사용
- `DEFAULT_FILE_STORAGE` 설정이 제대로 적용되지 않음

**해결 과정**:

1. **환경 변수 감지 개선**
   ```python
   # settings.py에서 환경 감지 로직 강화
   IS_APP_ENGINE = (
       os.environ.get('GAE_APPLICATION', None) or 
       os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine/')
   )
   ```

2. **Google Cloud Storage 설정 추가**
   ```python
   # requirements.txt 업데이트
   django-storages==1.14.4
   google-cloud-storage==2.10.0
   
   # settings.py Google Cloud Storage 설정
   if IS_APP_ENGINE:
       DEFAULT_FILE_STORAGE = 'storages.backends.gcloud.GoogleCloudStorage'
       GS_BUCKET_NAME = 'centerweb-project.appspot.com'
       GS_DEFAULT_ACL = 'publicRead'
   ```

3. **Django 4.2+ STORAGES 설정 적용**
   ```python
   # 최종 해결: Django 4.2+ 방식으로 변경
   STORAGES = {
       "default": {
           "BACKEND": "storages.backends.gcloud.GoogleCloudStorage",
       },
       "staticfiles": {
           "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
       },
   }
   ```

4. **디버깅 로깅 추가**
   ```python
   # 환경 변수 및 설정 상태 확인용 로그
   print(f"DEBUG: GAE_APPLICATION = {os.environ.get('GAE_APPLICATION', 'None')}")
   print(f"DEBUG: STORAGES 설정 완료 - {STORAGES}")
   ```

#### 2. 데이터베이스 세션 오류

**문제 상황**:
```
django.db.utils.OperationalError: no such table: django_session
```

**원인**:
- App Engine 재배포 시 `/tmp` 디렉토리 초기화
- 마이그레이션은 실행되지만 세션 테이블 누락

**해결방법**:
```python
# main.py에서 자동 마이그레이션 강화
call_command('migrate', verbosity=0, interactive=False)
# 추가 세션 테이블 생성 보장
call_command('migrate', 'sessions', verbosity=0, interactive=False)
```

#### 3. 배포 과정에서의 추가 최적화

**파일 업로드 경로 설정**:
```python
# models.py - 갤러리 이미지 업로드 경로
image = models.ImageField(upload_to='gallery/', blank=True, null=True)
```

**에러 처리 강화**:
```python
# views.py - 갤러리 업로드 에러 핸들링
try:
    post.save()
    messages.success(request, '갤러리 글이 성공적으로 업로드되었습니다.')
except Exception as e:
    import traceback
    print(f"갤러리 업로드 에러: {e}")
    print(f"상세 에러: {traceback.format_exc()}")
    messages.error(request, f'이미지 업로드 중 오류가 발생했습니다: {str(e)}')
```

### 배포 성과 및 학습 내용

#### 기술적 성과
- ✅ **Google Cloud Storage 통합**: 파일 업로드 시스템 완전 구현
- ✅ **App Engine 환경 최적화**: 읽기 전용 파일시스템 제약 극복
- ✅ **자동화된 배포 프로세스**: 마이그레이션, 관리자 계정 생성 자동화
- ✅ **환경별 설정 분리**: 개발/운영 환경 완전 분리

#### 학습한 핵심 개념
1. **클라우드 스토리지 통합**: Django-storages를 통한 Google Cloud Storage 연동
2. **App Engine 제약사항**: 읽기 전용 파일시스템과 임시 디렉토리 활용
3. **Django 4.2+ STORAGES**: 새로운 스토리지 설정 방식 적용
4. **배포 환경 디버깅**: 로그 기반 실시간 문제 해결

#### 최종 배포 구성
```yaml
# 최종 app.yaml
runtime: python311
env_variables:
  SECRET_KEY: "django-insecure-key"
  DEBUG: "True"  # 디버깅 시에만 True

# 최종 requirements.txt
Django==5.2.4
Pillow==11.3.0
gunicorn==21.2.0
django-storages==1.14.4
google-cloud-storage==2.10.0
```

---

**개발 기간**: 2024년 7월 14일 ~ 7월 25일 (12일)  
**배포 일시**: 2025년 7월 25일  
**추가 디버깅**: 2025년 7월 25일 (갤러리 업로드 기능 완성)  
**개발 인원**: 3명  
**프로젝트 상태**: ✅ **목표 일정 내 성공적 완료 및 운영 배포**
