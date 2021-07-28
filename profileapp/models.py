from django.contrib.auth.models import User
from django.db import models

# Create your models here.

# 0. pip install pillow
# 1. profile - account 1:1 매칭 시키기
# 2. migration 하기 python mange.py makemigrations
# 3. python mange.py migrate


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,  #CASCADE는 연결된 계정이 삭제되면 함께 삭제,
                                related_name='profile')
    image = models.ImageField(upload_to='profile/', null=True)
    nickname = models.CharField(max_length=30, unique=True)
    message = models.CharField(max_length=200, null=True)
