from django.urls import path
from . import views

urlpatterns =[
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('ad_process', views.ad_process, name='ad_process'),
    path('admission', views.admission, name='admission'),
    path('download', views.download, name='download'),
    path('contact', views.contact, name='contact'),
    path('notice', views.notice, name='notice'),
    path('teachers', views.teachers, name='teachers'),
    path('testimonials', views.testimonials, name='testimonials'),
    path('gallery', views.gallery, name='gallery')
    ]