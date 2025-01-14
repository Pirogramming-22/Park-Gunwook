from django.shortcuts import render, get_object_or_404, redirect
from .models import Idea, IdeaStar
from .forms import IdeaForm
from django.core.paginator import Paginator
from django.http import JsonResponse
import json

def idea_list(request):
    sort_by = request.GET.get('sort_by', 'like')  # 기본 정렬 기준은 'like'

    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    liked_ideas = IdeaStar.objects.filter(session_key=session_key).values_list('idea_id', flat=True)

    # 정렬 기준에 맞게 쿼리셋을 가져옵니다.
    if sort_by == 'like':
        ideas = Idea.objects.all().order_by('-like')  # like
    elif sort_by == 'name':
        ideas = Idea.objects.all().order_by('name')  # 이름순
    elif sort_by == 'created_at':
        ideas = Idea.objects.all().order_by('-created_at')  # 최신순
    elif sort_by == 'liked':  # 찜 여부에 따라 정렬
        # 찜한 아이디어가 먼저 나오도록 정렬
        ideas = sorted(Idea.objects.all(), key=lambda x: x.id in liked_ideas, reverse=True)
    else:
        ideas = Idea.objects.all()  # 기본 정렬 기준


    if not session_key:
        request.session.create()
    liked_ideas = IdeaStar.objects.filter(session_key=session_key).values_list('idea_id', flat=True)

    # 페이지네이션 처리
    paginator = Paginator(ideas, 4)  # 한 페이지에 4개의 아이디어
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'idea/idea_list.html', {'page_obj': page_obj, 'sort_by': sort_by, 'liked_ideas': liked_ideas})

def idea_detail(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    return render(request, 'idea/idea_detail.html', {'idea': idea})

def idea_create(request):
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES)
        if form.is_valid():
            idea = form.save()
            return redirect('idea_detail', idea_id = idea.id)
    else:
        form = IdeaForm()
    return render(request, 'idea/idea_create.html', {'form': form})

def idea_edit(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    if request.method == 'POST':
        form = IdeaForm(request.POST, request.FILES, instance=idea)
        if form.is_valid():
            form.save()
            return redirect('idea_detail', idea.id)
    else:
        form = IdeaForm(instance=idea)
    return render(request, 'idea/idea_edit.html', {'form': form})

def idea_delete(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)
    idea.delete()  # 개발툴 삭제
    return redirect('idea_list')  # 개발툴 목록 페이지로 리디렉션

def update_like(request, idea_id):
    if request.method == 'POST':
        idea = Idea.objects.get(id=idea_id)
        data = json.loads(request.body)  # 요청 본문에서 JSON 데이터 파싱
        action = data.get('action')

        # action에 따라 관심도 업데이트
        if action == 'increase':
            idea.like += 1
        elif action == 'decrease':
            idea.like -= 1

        idea.save()  # 변경된 관심도 저장

        # JSON 응답을 통해 새로운 관심도 반환
        return JsonResponse({
            'status': 'success',
            'new_like_count': idea.like
        })
    
def toggle_like(request, idea_id):
    idea = get_object_or_404(Idea, id=idea_id)

    # 세션 키를 가져옵니다.
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    # 찜 상태를 토글 (찜하거나 찜 해제)
    existing_star = IdeaStar.objects.filter(idea=idea, session_key=session_key).first()

    if existing_star:
        existing_star.delete()  # 찜 해제
        action = 'removed'
    else:
        IdeaStar.objects.create(idea=idea, session_key=session_key)  # 찜하기
        action = 'added'

    return JsonResponse({'status': action, 'idea_id': idea.id})