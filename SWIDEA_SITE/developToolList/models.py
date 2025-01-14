from django.db import models

# Create your models here.
class DevelopTool(models.Model):
    name = models.CharField('이름', max_length=30)
    languageType = models.CharField('종류', max_length=30)
    content = models.CharField('개발툴 설명', max_length=300)

    def __str__(self):
        return self.name
