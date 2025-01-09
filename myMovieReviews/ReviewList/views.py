# ReviewList/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import MovieReview
from .forms import MovieReviewForm

# 리뷰 리스트 페이지
def review_list(request):
    reviews = MovieReview.objects.all()
    return render(request, 'ReviewList/review_list.html', {'reviews': reviews})

# 리뷰 디테일 페이지
def review_detail(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    return render(request, 'ReviewList/review_detail.html', {'review': review})

# 리뷰 작성 페이지
def review_create(request):
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('review_list')  # 리뷰 리스트로 돌아가기
    else:
        form = MovieReviewForm()
    return render(request, 'ReviewList/review_form.html', {'form': form})

# 리뷰 수정 페이지
def review_edit(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, instance=review)
        if form.is_valid():
            form.save()
            return redirect('review_detail', pk=review.pk)  # 수정 후 디테일 페이지로 돌아가기
    else:
        form = MovieReviewForm(instance=review)
    return render(request, 'ReviewList/review_form.html', {'form': form})

# 리뷰 삭제
def review_delete(request, pk):
    review = get_object_or_404(MovieReview, pk=pk)
    review.delete()
    return redirect('review_list')  # 삭제 후 리뷰 리스트 페이지로 돌아가기
