from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
# Create your views here.

def IndexPage(request):
    return render(request,"app/index.html")


def Insert(request):
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    pics = request.FILES['image']

    newuser = user.objects.create(firstname=fname,lastname=lname,email=email,pics=pics)
    return HttpResponseRedirect(reverse('show'))


def AllData(request):
    alldata = user.objects.all()
    return render(request,"app/show.html",{'key1':alldata})



def getById(request,pk):
    getdata =user.objects.get(pk=pk)
    return render(request,"app/edit.html",{'key2':getdata})


def Update(request,pk):
    udata = user.objects.get(pk=pk)
    udata.firstname = request.POST['fname']
    udata.lastname = request.POST['lname']
    udata.email = request.POST['email']
    udata.save()
    return HttpResponseRedirect(reverse('show'))


def Delete(request,pk):
    ddata = user.objects.get(pk=pk)
    ddata.delete()
    return HttpResponseRedirect(reverse('show'))