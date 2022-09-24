from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse 
from .models import Contact,HomePosts,Gallery, Presskit,Tour
from django.contrib import messages

# Create your views here.
def home(request):
    home_obj= HomePosts.objects.all()[0:6]
    return render(request,'index.html',{'home_obj':home_obj})

def gallery(request):
    gallery_obj=Gallery.objects.all()
    return render(request,'gallery.html',{'gallery_obj':gallery_obj})

def tour(request):
    tour_obj=Tour.objects.all()
    return render(request,'tour.html',{'tour_obj':tour_obj})

def presskit(request):
    pkit_obj=get_object_or_404(Presskit,id=1)
    return render(request,'pkit.html',{'pkit_obj':pkit_obj})

def contact(request):
    if request.method == "POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        entry=Contact(name=name,email=email,phone=phone,
        subject=subject,message=message)
        entry.save()
        messages.success(request,'Success,Thx for contacting!')
        return HttpResponseRedirect(reverse('contact'))
    return render(request,'contact.html')