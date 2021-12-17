# Generated by Django 3.2.7 on 2021-12-17 03:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0005_auto_20211216_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='Nội dung'),
        ),
        migrations.AlterField(
            model_name='message',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='message',
            name='is_read',
            field=models.BooleanField(default=False, null=True, verbose_name='Đã đọc'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='messages', to='users.profile', verbose_name='Người nhận'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile', verbose_name='Người gửi'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tiêu đề'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(blank=True, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(blank=True, max_length=500, null=True, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Địa chỉ'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, default='profiles/user-default.png', null=True, upload_to='profiles/', verbose_name='Ảnh mô tả'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='short_intro',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Mô tả ngắn'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_github',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Github cá nhân'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_linkedin',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Linkedin cá nhân'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_twitter',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Twitter cá nhân'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_website',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Website cá nhân'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='social_youtube',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Youtube cá nhân'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Người dùng'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên đăng nhập'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Mô tả'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Tên'),
        ),
        migrations.AlterField(
            model_name='skill',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.profile', verbose_name='Người sở hữu'),
        ),
    ]
