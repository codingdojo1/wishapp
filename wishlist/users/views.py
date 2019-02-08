from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserLogin
from .models import userManamege

# Create your views here.
def new(req):
  return render(req, 'users/new.html')

def create(req):
  errors = userManamege.validate_reg(req.POST)
  existing_users = UserLogin.objects.filter(email=req.POST['email'])
  if existing_users:
    errors.append("Email already in use")
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')
  user = userManamege.create_user(req.POST)
  req.session['user_id'] = user.id
  return redirect('wishes:index')

def login(req):
  errors = UserLogin.objects.validate_login(req.POST)
  if errors:
    for error in errors:
      messages.error(req, error)
    return redirect('users:new')

  valid, result = UserLogin.objects.login(req.POST)
  if not valid:
    messages.error(req, result)
    return redirect('users:new')
  else:
    req.session['user_id'] = result.id
  return redirect('wishes:index')

def logout(req):
  req.session.clear()
  return redirect('users:new')
