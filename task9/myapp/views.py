from django.shortcuts import render
from django.http import HttpResponse

def homepageview(request):
    return render(request,'home.html')

def aboutpageview(request):
    return render(request,'about.html')

def contactpageview(request):
    return render(request,'contact.html')

def form(request):
    return render(request,'form.html')

def process(request):
    print("hi")
    print(request.method)
    print(request.POST)
    a=(request.POST['txt1'])
    b=(request.POST['txt2'])
    c=int(request.POST['txt3'])
    d=(request.POST['txt4'])
    
    return render(request,'ans.html',{'fName':a,'lName':b,'contact':c,'email':d})

