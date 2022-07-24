from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')


def notice(request):
    return render(request, 'notice.html')


def teachers(request):
    return render(request, 'teachers.html')


def gallery(request):
    return render(request, 'gallery.html')


def testimonials(request):
    return render(request, 'testimonials.html')

def about(request):
    return render(request, 'about.html')


def ad_process(request):
    return render(request, 'ad_process.html')


def admission(request):
    return render(request, 'admission.html')


def contact(request):
    return render(request, 'contact.html')


def download(request):
    return render(request, 'download.html')
