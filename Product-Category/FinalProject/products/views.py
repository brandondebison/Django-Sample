from django.shortcuts import render, redirect
from .models import Product
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .import forms



# Create your views here.

def product_list(request):
    products = Product.objects.all()  #.order_by()
    return render(request,'products/product_list.html', {'products': products})
    
def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    return render(request, 'products/product_detail.html', {'product':product})



@login_required(login_url="/accounts/login/")
def product_create(request):
    if request.method =='POST':
        form = forms.CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('products:list')
    else:
        form = forms.CreateProduct
    return render(request, 'products/product_create.html',{'form':form})