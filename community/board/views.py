from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.http import Http404
from user.models import User
from tag.models import Tag
from .models import Board
from .forms import BoardForm


# Create your views here.
def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('게시물을 찾을 수 없습니다.')
    return render(request, 'board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/user/login')
    if request.method == 'POST':
        form = BoardForm(request.POST)
        if form.is_valid():
            user_id = request.session.get('user')
            user = User.objects.get(pk=user_id)

            tags = form.cleaned_data['tags'].split(',')

            board = Board()
            board.title = form.cleaned_data['title']
            board.contents = form.cleaned_data['contents']
            board.writer = user
            board.save()

            for tag in tags:
                if not tag:
                    continue
                # 모델에 있으면 가져오고 없으면 생성 후 가져온다.
                # 파이썬에서 사용하지 않는 변수는 _ 세팅한다.
                _tag, _ = Tag.objects.get_or_create(name=tag)
                board.tags.add(_tag)
            return redirect('/board/list')
    else:
        form = BoardForm()
    return render(request, 'board_write.html', {'form': form})


def boar_list(request):
    all_boards = Board.objects.all().order_by('-id')
    page = request.GET.get('p', 1)
    paginator = Paginator(all_boards, 2)
    boards = paginator.get_page(page)
    return render(request, 'board_list.html', {'boards': boards})
