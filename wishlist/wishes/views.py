import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Wish
# Create your views here.
def index(req):
    if not req.user.is_authenticated():
        return redirect('users:new')
    return render(req, 'wishes/index.html', {"wishes": Wish.objects.all()})

context = {
    # 'wish_list': Wish.objects.exclude(creator=req.session['user_id']),
    # 'grant_list':,
}

def new(req):
    return render(req, 'wishes/new.html')

def grant(request):
    wish = Wish.objects.get(id=request.POST.get("wish_id"))
    wish.granted_at = datetime.datetime.now()
    wish.save()
    return redirect('wishes:index')

def create(request):
  print(request.user)
  data = {
    "name": request.POST.get("name"),
    "description": request.POST.get("description"),
    "creator": request.user
  }
  wish = Wish.objects.create(**data)
  from django.http import HttpResponse
  return redirect('wishes:index')
    #  return redirect('wishes:index')

# def create(req):
#   errors = Product.objects.validate(req.POST)
#   if errors:
#     for error in errors:
#       messages.error(req, error)
#     return redirect('wishes:new')
#   # create the product if there are no errors
#   Product.objects.create_product(req.POST, req.session['user_id'])
#   return redirect('wishes:index')

def edit(req):
    pass

def upadate(req):
    pass

def delete(req):
    pass
