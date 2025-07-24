# board/models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    BOARD_CHOICES = [
        ('general', '일반게시판'),
        ('gallery', '갤러리'),
        ('admin', '관리자게시판'),
    ]
    
    title = models.CharField(max_length=200, verbose_name='제목')
    content = models.TextField(verbose_name='내용')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='작성자')
    board_type = models.CharField(max_length=20, choices=BOARD_CHOICES, default='general', verbose_name='게시판 구분')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
    views = models.PositiveIntegerField(default=0, verbose_name='조회수')
    likes = models.PositiveIntegerField(default=0, verbose_name='좋아요')
    
    # 갤러리용 이미지 필드
    image = models.ImageField(upload_to='gallery/', blank=True, null=True, verbose_name='이미지')
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = '게시글'
        verbose_name_plural = '게시글'
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('board:post_detail', kwargs={'pk': self.pk})
    
    def increment_views(self):
        """조회수 증가"""
        self.views += 1
        self.save(update_fields=['views'])
    
    def increment_likes(self):
        """좋아요 증가"""
        self.likes += 1
        self.save(update_fields=['likes'])