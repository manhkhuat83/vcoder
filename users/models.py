from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
import uuid

# Create your models here.
class Profile(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Người dùng')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tên')
    email = models.EmailField(max_length=500, blank=True, null=True, verbose_name='Email')
    username = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tên đăng nhập')
    location = models.CharField(max_length=200, blank=True, null=True, verbose_name='Địa chỉ')
    short_intro = models.CharField(max_length=200, blank=True, null=True, verbose_name='Mô tả ngắn')
    bio = models.TextField(blank=True, null=True, verbose_name='Mô tả')
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/user-default.png", verbose_name='Ảnh mô tả')
    social_github = models.CharField(max_length=200, blank=True, null=True, verbose_name='Github cá nhân')
    social_twitter = models.CharField(max_length=200, blank=True, null=True, verbose_name='Twitter cá nhân')
    social_linkedin = models.CharField(max_length=200, blank=True, null=True, verbose_name='Linkedin cá nhân')
    social_youtube = models.CharField(max_length=200, blank=True, null=True, verbose_name='Youtube cá nhân')
    social_website = models.CharField(max_length=200, blank=True, null=True, verbose_name='Website cá nhân')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')

    def __str__(self):
        return str(self.username)

    class Meta:
        verbose_name_plural = 'Hồ sơ cá nhân'
        ordering = ['created',]

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url


class Skill(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, blank=True, verbose_name='Người sở hữu')
    name = models.CharField(max_length=200, blank=True, null=True, verbose_name='Tên')
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')
    
    class Meta:
        verbose_name_plural = 'Kỹ năng'
    
    def __str__(self):
        return str(self.name)


class Message(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Người gửi')
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True, blank=True, related_name="messages", verbose_name='Người nhận')
    name = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tên')
    email = models.EmailField(max_length=200, null=True, blank=True, verbose_name='Email')
    subject = models.CharField(max_length=200, null=True, blank=True, verbose_name='Tiêu đề')
    body = models.TextField(verbose_name='Nội dung')
    is_read = models.BooleanField(default=False, null=True, verbose_name='Đã đọc')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')
    
    class Meta:
        verbose_name_plural = 'Tin nhắn'
    
    def __str__(self):
        return self.subject

    class Meta:
        ordering = ['is_read', '-created']