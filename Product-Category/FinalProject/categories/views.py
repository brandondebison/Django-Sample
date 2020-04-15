from django.shortcuts import render, redirect
from .models import Category
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms




# Create your views here.

def categories(request):

    categories = Category.objects.all()  #.order_by()
    return render(request,'categories/categories.html', {'categories':categories})

def catergory_detail(request, slug):
    return HttpResponse(slug)


@login_required(login_url="/accounts/login/")
def catergory_create(request):
    if request.method =='POST':
        form = forms.CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('categories:list')
    else:
        form = forms.CreateCategory
    return render(request, 'categories/category_create.html',{'form':form})