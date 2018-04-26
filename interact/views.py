from django.http import HttpResponse
from django.shortcuts import render, redirect
from django import forms
from .forms import Inputlog
from django.core.mail import EmailMessage

# Create your views here.


def index(request):
    if request.method == 'GET':
         user_form = Inputlog(request.GET)
         return render(request, 'page.html', {
        'user_form': user_form    #user_form
      })

    if request.method == 'POST':
        user_form1 = Inputlog(request.POST)
        
        if user_form1.is_valid() :
           ab="post chala"       
     
           #prof= profile_form.save()
           light = user_form1.cleaned_data['light']
           #profile=profile_form.save(commit=False)
           #profile.user_id=user1.id+1
           #profile.college=profile_form.cleaned_data['college']
           #profile.save()
         
           if light=="0" :
             msg="lights are off"
             print ("off the light")
           else:
             msg="lights are on"
             
             print ("On the light")
           
    return render(request, 'page.html', {'user_form': user_form1,'msg':msg })


