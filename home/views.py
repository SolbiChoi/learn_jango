from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    path = request.path
    resultstr = ''
    if path == '/home':
        resultstr = '<h1>여기는 home 입니다.</h1>'
    else:
        resultstr = '<h1>여기는 최솔비 입니다.</h1>'

    return HttpResponse(resultstr)

def index01(request):
    result = {'first':'Solbi','second':'Choi'}
    return render(request, 'index.html', context=result)

def index02(request):
    # result = {'first':request.GET['first'],'second':request.GET['second']}
    return render(request, 'index_copy.html')