from django.db import models

# Create your models here.


# models 라는 모듈안에 Model 클래스를 불러오는 것
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null=False)