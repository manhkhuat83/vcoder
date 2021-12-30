from django.db import models
from users.models import Profile
import uuid

# Create your models here.
class Project(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.CASCADE, verbose_name='Người sở hữu')
    title = models.CharField(max_length=200, verbose_name='Tiêu đề')
    description = models.TextField(null=True, blank=True, verbose_name='Mô tả')
    featured_image = models.ImageField(null=True, blank=True, default="default.jpg", verbose_name='Ảnh mô tả')
    demo_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Link demo')
    source_link = models.CharField(max_length=2000, null=True, blank=True, verbose_name='Source code')
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='Thẻ')
    role = models.CharField(max_length=255, blank=True, null=True, verbose_name='Vai trò')
    vote_total = models.IntegerField(default=0, null=True, blank=True, verbose_name='Tổng số bầu')
    vote_ratio = models.IntegerField(default=0, null=True, blank=True, verbose_name='Tỷ lệ bầu')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural= 'Dự án'
        ordering = ['-vote_ratio', '-vote_total', 'title']

    @property
    def imageURL(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id', flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVotes = reviews.filter(value='up').count()
        totalVotes = reviews.count()
        ratio = (upVotes / totalVotes) * 100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()


class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Tích cực'),
        ('down', 'Tiêu cực'),
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, verbose_name='Người sở hữu')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Dự án')
    body = models.TextField(null=True, blank=True, verbose_name='Nội dung')
    value = models.CharField(max_length=200, choices=VOTE_TYPE, verbose_name='Giá trị bầu')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')

    class Meta:
        verbose_name_plural= 'Đánh giá'
        unique_together = [['owner', 'project']]

    def __str__(self):
        return self.value


class Tag(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True,primary_key=True, editable=False)
    name = models.CharField(max_length=200, verbose_name='Tên thẻ')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Thời gian tạo')

    class Meta:
        verbose_name_plural= 'Thẻ'
    
    def __str__(self):
        return self.name

