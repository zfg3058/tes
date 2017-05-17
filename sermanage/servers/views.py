from django.shortcuts import render,render_to_response
from django.http import HttpResponse

# Create your views here.

def sertest(request):
    return HttpResponse('test!!!')

def loginst(request):
    return render_to_response('test.html')