from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
import json
from django.contrib import messages
from .models import *
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from .form import CreateUsers

# Create your views here.

def register(request):
    form = CreateUsers()

    if request.method == 'POST':
        form = CreateUsers(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username', 'password')
            messages.success(request, 'Success on creating ' + user)
            return redirect('/login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Username or Password is incorrect')
    context = {}
    return render(request, 'login.html', context)

def index(request):
    products = Product.objects.all()
    context = {
        'products':products,
    }
    return render(request, 'home.html', context)

def logout(request):
    request.session.clear()
    return redirect('/login')

def product(request, product_id):
    my_product = Product.objects.get(id=product_id)
    context = {
        'product': my_product
    }
    return render(request, 'product.html', context)

def create(request):
    Product.objects.create(
        title =request.POST['title'],
        price =request.POST['price'],
        image =request.POST['image'],
    )
    return redirect('/')

def checkout(request):
    
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, finished=False) 
        items = order.customerproduct_set.all()
    else:
        items = []
        order = {'cart_total':0,'cart_total_items':0}

    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'checkout.html', context)

def user(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, finished=False) 
        items = order.customerproduct_set.all()
    else:
        items = []
        order = {'cart_total':0,'cart_total_items':0}
    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'user.html', context)

def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, finished=False) 
        items = order.customerproduct_set.all()
    else:
        items = []
        order = {'cart_total':0,'cart_total_items':0}

    context = {
        'items':items,
        'order':order,
    }
    return render(request, 'cart.html', context)

def updateOrder(request):
    # customer = request.user.customer
    # product = Product.objects.get(id=product_id)
    # order, created = Order.objects.get_or_create(customer=customer, finished=False) 

    # customerProduct, created = CustomerProduct.objects.get_or_create(order=order, product=product)
    return JsonResponse('Item was added', safe=False)