from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Category

# Create your views here.

def cat(req):
    return redirect('show_cat')
def insert(req):
    cat_name = req.POST.get('cat_name').lower()
    if Category.objects.filter(name=cat_name).exists():
        return HttpResponse('existed')
    else:
        cat_obj = Category()
        cat_obj.name = cat_name
        # Category.objects.create(name=cat_name)
        cat_obj.save()

        return redirect('show_cat')
    return HttpResponse(cat_name)

def cat_show(req):
    all_cat = Category.objects.all()
    all_data = {'all_cat':all_cat}
    return render(req,'cat.html',all_data)
def update(req):
    return HttpResponse("cat_update")
def delete(req):
    return HttpResponse("cat_delete")
