from django.shortcuts import render

# Create your views here.
def boar_list(request):
    return render(request, 'board_list.html')
