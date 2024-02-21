from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def next(request):
    return render(request, 'main/next.html')