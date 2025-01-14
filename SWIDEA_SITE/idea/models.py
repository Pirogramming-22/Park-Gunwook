from django.db import models
from developToolList.models import DevelopTool
from django.core.exceptions import ValidationError

# Create your models here.
class Idea(models.Model):
    name = models.CharField('아이디어명', max_length=30)
    image = models.ImageField('image', upload_to='images/%Y%m%d', blank=True, null=True)
    ideaContent = models.CharField('아이디어 설명', max_length=300)
    like = models.IntegerField('아이디어 관심도', default=0)
    developTool = models.ForeignKey(DevelopTool, on_delete=models.CASCADE, related_name='developmentTool', verbose_name='예상 개발툴')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    def clean(self):
        # image 필드가 비어있으면 ValidationError 발생
        if not self.image:
            raise ValidationError('이미지를 반드시 입력해야 합니다.')

class IdeaStar(models.Model):
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name='stars')  # 찜한 아이디어
    session_key = models.CharField(max_length=255)  # 세션 키를 기반으로 찜 상태를 구분

    def __str__(self):
        return f"{self.session_key} - {self.idea.name} 찜"