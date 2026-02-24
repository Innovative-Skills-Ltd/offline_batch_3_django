from django.shortcuts import render,redirect
from django.http import HttpResponse
from category.models import Category
from subcategory.models import SubCategory

# Create your views here.

def subcat(req):
    all_cat = Category.objects.all()
    all_subcat = SubCategory.objects.all()
    all_subcat_rel = SubCategory.objects.select_related('category').all()
    all_data = {'all_cat':all_cat,'all_subcat':all_subcat,'all_subcat_rel':all_subcat_rel}

    return render(req,'subcat.html',all_data)
def insert(req):
    cat_id = req.POST.get('cat_id')
    sub_cat_name = req.POST.get('subcategory_name')
    category_instance = Category.objects.get(id=cat_id)
    SubCategory.objects.create(category=category_instance,sub_cat_name=sub_cat_name)
    return  redirect('show_subcat')