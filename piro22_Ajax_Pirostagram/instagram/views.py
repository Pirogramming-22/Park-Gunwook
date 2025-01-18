from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from .models import Post, Comment, Like

# 메인 페이지 (게시물 목록)
def main_page(request):
    posts = Post.objects.all()
    return render(request, 'instagram/main_page.html', {'posts': posts})
# 댓글 추가
@require_POST
def add_comment(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    content = request.POST.get('content')

    # 댓글을 작성한 유저를 로그인한 사용자로 지정
    comment = Comment.objects.create(post=post, content=content)

    # 댓글 추가 후 JSON 응답 (ID 포함)
    return JsonResponse({
        'id': comment.id,
        'content': comment.content,
        'created_at': comment.created_at.strftime('%Y-%m-%d %H:%M:%S')  # 댓글 작성 시간을 포맷
    })



# 댓글 삭제
@require_POST
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    
    # 댓글 삭제
    comment.delete()

    # 댓글 삭제 후 JSON 응답
    return JsonResponse({'status': 'success'})

# 좋아요 추가/삭제
def toggle_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    # DB에서 좋아요 상태 확인
    existing_like = Like.objects.filter(post=post).first()

    if(request.method == "POST"):
        if existing_like:
            # 이미 좋아요가 되어 있으면 좋아요 취소
            existing_like.delete()
            status = 'unliked'
        else:
            # 좋아요가 없으면 좋아요 추가
            Like.objects.create(post=post)
            status = 'liked'
    else:
        if existing_like:
            status = 'liked'
        else:
            status = 'unliked'

    # 좋아요 개수 업데이트
    likes_count = post.likes.count()
    print(likes_count)

    return JsonResponse({'status': status, 'likes_count': likes_count})