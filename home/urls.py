from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('gallery/',views.gallery,name='gallery'),
    path('tour/',views.tour,name='tour'),
    path('pkit/',views.presskit,name='presskit'),
    path('contact/',views.contact,name='contact')
    
]