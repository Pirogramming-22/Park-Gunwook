from django.shortcuts import render, get_object_or_404, redirect
from .models import DevelopTool
from .forms import DevelopToolForm

def developtool_list(request):
    tools = DevelopTool.objects.all()
    return render(request, 'developToolList/developtool_list.html', {'tools': tools})

def developtool_detail(request, developtool_id):
    tool = get_object_or_404(DevelopTool, id=developtool_id)
    ideas = tool.developmentTool.all()
    return render(request, 'developToolList/developtool_detail.html', {'tool': tool, 'ideas': ideas})

def developtool_create(request):
    if request.method == 'POST':
        form = DevelopToolForm(request.POST)
        if form.is_valid():
            developtool = form.save()
            return redirect('developtool_detail', developtool_id=developtool.id)
    else:
        form = DevelopToolForm()
    return render(request, 'developToolList/developtool_create.html', {'form': form})

def developtool_edit(request, developtool_id):
    tool = get_object_or_404(DevelopTool, id=developtool_id)
    if request.method == 'POST':
        form = DevelopToolForm(request.POST, instance=tool)
        if form.is_valid():
            form.save()
            return redirect('developtool_detail', tool.id)
    else:
        form = DevelopToolForm(instance=tool)
    return render(request, 'developToolList/developtool_edit.html', {'form': form})

def developtool_delete(request, developtool_id):
    tool = get_object_or_404(DevelopTool, id=developtool_id)
    tool.delete()  # 개발툴 삭제
    return redirect('developtool_list')  # 개발툴 목록 페이지로 리디렉션