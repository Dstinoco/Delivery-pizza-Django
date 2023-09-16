from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def produto(request):
    return render(request, 'produto.html')