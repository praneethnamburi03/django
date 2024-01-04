from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.contrib import messages 
from new1.models import student
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm

# Create your views here.
def register(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'welcome user {username} your account is created')
            '''s=student.objects.all()
            context={
                's':s,
            }
            return render(request,'food/index.html',context)'''
            return redirect('login')

    else:
        form=RegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profilepage(request):
    return render(request,'users/profile.html')