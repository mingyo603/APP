from django.db import models
from django.conf import settings
from accounts.models import User

# Create your models here.

class Blog(models.Model):
    # 1. 게시글의 id 값
    id = models.AutoField(primary_key=True, null=False, blank=False) 
    # 2. 제목
    title = models.CharField(max_length=100)
    # 3. 작성일
    created_at = models.DateTimeField(auto_now_add=True)
    # 4. 작성자
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    # 5. 본문
    body = models.TextField()
# test
# 이미지 업로드 경로 지정 함수
def blog_image_upload_path(instance, filename):
    return f'blog/{instance.blog.id}/{filename}'

# 블로그 이미지 모델 (다중 이미지용)
class BlogImage(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=blog_image_upload_path)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return f'Image for blog ID {self.blog.id}'
