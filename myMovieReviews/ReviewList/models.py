from django.db import models

class MovieReview(models.Model):
    title = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    cast = models.CharField(max_length=200)
    genre = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    runtime = models.PositiveIntegerField()  # 러닝타임 (분 단위)
    review_content = models.TextField()  # 리뷰 내용
    release_year = models.PositiveIntegerField()