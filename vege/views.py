from django.shortcuts import render, redirect
from vege.models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url = "/")
def receipes(request):
  if request.method == "POST":
    data = request.POST
    receipe_image = request.FILES.get('receipe_image')
    recipe_name = data.get('recipe_name')
    receipe_description = data.get('receipe_description')
    Recipe.objects.create(
     recipe_name = recipe_name, 
     receipe_description = receipe_description,
     receipe_image = receipe_image
    )
    return redirect('/receipe/')
  

  queryset = Recipe.objects.all()

  if request.GET.get('search'):
    queryset = queryset.filter(recipe_name__icontains = request.GET.get('search') )

  context = {'receipes' : queryset}
  return render(request, "receipes.html", context)


@login_required(login_url = "/")
def update_receipe(request, id):
  queryset = Recipe.objects.get(id = id)
  if request.method == "POST":
    data = request.POST
    receipe_image = request.FILES.get('receipe_image')
    recipe_name = data.get('recipe_name')
    receipe_description = data.get('receipe_description')
    queryset.recipe_name = recipe_name
    queryset.receipe_description = receipe_description
    if receipe_image:
      queryset.receipe_image = receipe_image
    queryset.save()
    return redirect('/receipe/')
  context = {'receipe' : queryset}
  return render(request, "update-receipes.html", context)


@login_required(login_url = "/")
def delete_receipe(request, id):
  queryset = Recipe.objects.get(id = id)
  queryset.delete()
  return redirect('/receipe/') 




def login_page(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')

    if not User.objects.filter(username = username).exists():
      messages.info(request, "Invalid Username.")
      return redirect('')
    
    user = authenticate(username = username, password = password)

    if user is None:
      messages.info(request, "Invalid Password.")
      return redirect('') 
    else:
      login(request,  user) 
      return redirect('/receipe/')

  return render(request, "login.html")


def logout_page(request):
  logout(request)
  return redirect('/')


def register_page(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = User.objects.filter(username = username)

    if user.exists():
      messages.info(request, "Username already Exists.")
      return redirect('/register/')
    


    user = User.objects.create(
     first_name = first_name,
     last_name = last_name,
     username = username,
    )

    user.set_password(password)
    user.save()

    messages.info(request, "Account Created Successfully.")

    return redirect('/register/')

  return render(request, "register.html")