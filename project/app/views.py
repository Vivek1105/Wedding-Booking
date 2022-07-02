import email
from email import message
from django.shortcuts import render,HttpResponse
from app.models import Contact


# Create your views here.

def home(request):
    return render(request, 'home.html')
def about(request):
    return render(request, 'about.html')
def service(request):
    return render(request, 'service.html')
def wedding(request):
    return render(request, 'wedding.html')
# def wedding(request):
#     return render(request, 'wedding.html')
def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        message=request.POST['message']

        var1=Contact(name=name,phone=phone,email=email,message=message)
        var1.save()
        print("data written suscessfully")
    return render(request, 'contact.html')
