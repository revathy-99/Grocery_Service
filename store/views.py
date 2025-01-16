from django.shortcuts import render, redirect
from .models import Product, Cart
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Display products
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

# Display a user's cart
@login_required
def cart(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'store/cart.html', {'cart_items': cart_items, 'total_price': total_price})

# Add a product to the cart
@login_required
def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    messages.success(request, "Product added to cart!")
    return redirect('product_list')

# Remove product from cart
@login_required
def remove_from_cart(request, product_id):
    cart_item = Cart.objects.get(user=request.user, product_id=product_id)
    cart_item.delete()
    messages.success(request, "Product removed from cart!")
    return redirect('cart')

# Register a new user
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        return redirect('product_list')
    return render(request, 'store/register.html')

# Login a user
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product_list')
        else:
            messages.error(request, "Invalid username or password")
    return render(request, 'store/login.html')

# Logout a usercd
def logout_user(request):
    logout(request)
    return redirect('product_list')
 
"""def addproduct(request):
    try:
        Name=request.POST['name']
        Description=request.POST['description']
        Price=request.POST['price']
        Image=request.POST['image']
        Category=request.POST['category']
        prodobj=Product.objects.create(name=Name,description=Description,price=Price,image=Image,category=Category)
        prodobj.save()
        return render(request,'product.html',{'msg':"created successfully"})
    except Exception as e:
        print(e)
    return render(request,'product.html',{'msg':"not created"})  

def display(request):
    proddtls=Product.objects.all()
    return render(request,'product.html',{'prod':proddtls})

def delete(request,pid):
    empdtls=Product.objects.get(id=pid)
    empdtls.delete()
    return render(request,'product.html',{'msg':"not deleted"}) 


def updatename(request):
    #update using filter
    try: 
        oldname=request.POST['oldname']
        newname=request.POST['newname']
        prod=Product.objects.filter(name=oldname)
        if prod.exists():
            prod.update(name=newname)
            return render(request,'product.html',{'msg1':'updated'})
        else:
            return render(request,'product.html',{'msg1':'no record found'})
    except Exception as e:
        print(e)
        return render(request,'product.html',{'msg1':'not updated'})"""