from django.shortcuts import render
import os
import sys

base_path = os.getcwd()
sys.path.append(base_path)


# Create your views here.

def demo(request):
    context = {}
    context['hello'] = "看看吧"
    return render(request, 'demo.html', context)
