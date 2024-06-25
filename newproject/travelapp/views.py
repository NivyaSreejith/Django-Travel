from django.http import HttpResponse
from django.shortcuts import render
from . models import Property
# Create your views here.

def demo(request):
    obj=Property.objects.all()
    return render (request,'index.html',{'result':obj})

#def about(request):
   # return render (request,'about.html')

#def contact(request):
    #return HttpResponse ('hello world')

#def detail(request):
    #return HttpResponse('details')

#def thanks(request):
    #return render (request,'thanks.html')

#def operations(request):
    #x=int(request.GET['num1'])
    #y=int(request.GET['num2'])
    #add_res=x+y
    # sub_res=x-y
    # mul_res=x*y
    # div_res=x/y
    # return render(request,'result.html',{'addition':add_res,'subtraction':sub_res,'multiplication':mul_res,'division':div_res})






