from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .models import student
from django.contrib import messages 
from .forms import studentform
from django.contrib.auth.decorators import login_required
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
# Create your views here.
@login_required
def view(request):
    s=student.objects.all()
    #x=loader.get_template('food/index.html')
    context={
        's':s,
    }
    #return HttpResponse(x.render(context,request))
    return render(request,'food/index.html',context)
    
    #return HttpResponse('<h1>hello world</h1>')
#@login_required
class IndexClassView(ListView):
    model = student;
    template_name='food/index.html'
    context_object_name='s'
    
def newone(request):
    return HttpResponse("new one")
def studentid(request,id1):
    ids=student.objects.get(pk=id1)
    context={
        'ids':ids,
    }
    #return HttpResponse('this id is %s'%id)
    return render(request,'food/details.html',context)
class detailOfStudent(DetailView):
    model = student;
    template_name='food/details.html'
    
def fun():
    s=student.objects.all()
    context={
        's':s,
    }
    return context
    
        
def newstudent(request):
    form=studentform(request.POST or None)
    if form.is_valid():
        form.save()
        '''s=student.objects.all()
        context={
            's':s,
        }
        #return redirect('new1:index')'''
        messages.success(request,f'student is added')
        return redirect("new1:view")
        #return render(request,'food/index.html',{'form':form})
    return render(request,'food/student-form.html',{'form':form})
class CreateStudent(CreateView):
    model=student
    fields=['id','name','age','marks','pics']
    template_name='food/student-form.html'
    def form_valid(self,form):
        form.instance.user_name=self.request.user
        return super().form_valid(form)
    
        
        

def editstudent(request,id):
    stu=student.objects.get(id=id)
    form=studentform(request.POST or None,instance=stu)
    if form.is_valid():
        form.save()
        #return render(request,'food/index.html',fun())
        return redirect("new1:view")
    return render(request,'food/student-form.html',{'form':form,'stu':stu})
def deletestudent(request,id):
    stu=student.objects.get(id=id)
    if request.method=='POST':
        stu.delete()
        return redirect('new1:view')
    return render(request,'food/deletestu.html',{'stu':stu})
    
