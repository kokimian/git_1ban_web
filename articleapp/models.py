from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article', null=True)
    project = models.ForeignKey(Project, on_delete=models.SET_NULL,  # 게시판이 삭제되도 아티클은 남겨두겠는데, 어디에도 소속되어있지않은 상태로
                                related_name='article', null=True)  # 게시판에서 게시글로 접근하는 이름이 related_name='article'
                                                                    # 모델 변경사항 생기면 migration 필요
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='article/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)

    like = models.IntegerField(default=0)

