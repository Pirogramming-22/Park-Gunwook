from django import forms
from .models import MovieReview

class MovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['title', 'director', 'cast', 'genre', 'rating', 'runtime', 'review_content', 'release_year']
        labels = {
            'title': '제목',
            'director': '감독',
            'cast': '주연',
            'genre': '장르',
            'rating': '평점',
            'runtime': '상영 시간',
            'review_content': '리뷰 내용',
            'release_year': '개봉 연도'
        }
