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
- **최종 제출**: 목표 일정 내 성공적 완료 ✅
- 📋 [QA 요청 문서](https://docs.google.com/presentation/d/15l9z946mHTCSn7FTQYzodXyT3QAiSB1OdqPsf2xuq0k/edit)

## 🛠 기술 스택

- **Backend**: Django 4.x
- **Database**: MariaDB → Django ORM (SQLite)
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Authentication**: Django Auth System

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
- ✅ 회원가입
- ✅ 로그인/로그아웃
- ✅ 프로필 관리
- ✅ 권한 관리 (일반사용자/관리자)

### 게시판 시스템
- ✅ 일반게시판 (로그인 사용자만 작성 가능)
- ✅ 갤러리 (이미지 업로드 지원)
- ✅ 관리자게시판 (관리자 권한 필요)
- ✅ 조회수, 좋아요 기능
- ✅ 페이징 처리

## 🔧 설치 및 실행

```bash
# 프로젝트 클론
git clone [repository-url]
cd CenterWeb

# 가상환경 생성 및 활성화
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install django pillow

# 데이터베이스 마이그레이션
python manage.py makemigrations
python manage.py migrate

# 관리자 계정 생성
python manage.py createsuperuser

# 서버 실행
python manage.py runserver
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
- ✅ **체계적인 프로젝트 관리**: PM 역할로 효율적 일정/프로세스 관리
- ✅ **표준화된 개발 프로세스**: 산출물 양식 제공으로 일관된 문서화
- ✅ **시퀀스 다이어그램 기반 체계적 개발**
- ✅ **Django 표준 아키텍처 적용**
- ✅ **모듈별 역할 분담을 통한 효율적 협업**
- ✅ **문제 해결 과정에서 기술적 성장**
- ✅ **개발 통합 관리로 성공적 프로젝트 완료**

---

**개발 기간**: 2024년 7월 14일 ~ 7월 25일 (12일)  
**목표 마감일**: 2024년 7월 25일 (과제 제출 마감)  
**개발 인원**: 3명  
**프로젝트 상태**: ✅ **목표 일정 내 성공적 완료 예정**
