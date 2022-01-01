from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'main.html')

def upload(request):
    return render(request, "upload_moive.html")

def video_compared(request):
    return render(request, "video_compared.html")

def test_list(request):
    return render(request, "test_list.html")
