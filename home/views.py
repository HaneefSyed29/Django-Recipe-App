from django.shortcuts import render, redirect
from django.http import HttpResponse
from .utils import send_email_to_client

# Create your views here.
def send_email(request):
  send_email_to_client()
  return redirect('home/')


def myHome(request):
  # we can also pass html in the https response
   
  peoples = [
    {"name" : "haneef", "age" : 21},
    {"name" : "fazal", "age" : 22}
  ]
  return render(request, "home/index.html", context = {'peoples':peoples})

def contact(request):
  return render(request, "home/contact.html")

def about(request):
  return render(request, "home/about.html")

def success_page(request):
  return HttpResponse("<h1>This is the Success page</h1>")
  
