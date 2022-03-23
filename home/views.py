from django.shortcuts import render,HttpResponse
from xml.etree.ElementInclude import include
from home.models import Home
# Create your views here.
def index(request):
    context={
        "variable":"this variable was added via context "
    }
    if request.method=="POST":
        username=request.POST.get('username')
        branch=request.POST.get('branch')
        cgpa=request.POST.get('cgpa')
        email=request.POST.get('email')
        password=request.POST.get('password')
        home_=Home(username=username,branch=branch,cgpa=cgpa,email=email,password=password)
        home_.save()
    return render(request,'index.html',context)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request,'about.html')
    # return HttpResponse("this is the about")

def services(request):
    return HttpResponse("you are in the services page")
def contact(request):
    return render(request,'contact.html')