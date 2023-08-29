from django.shortcuts import render, redirect
from .models import Product, Cart, ProductCart, Payment
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#show prodcut list
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})
#show cart
def cart_view(request):
    if request.user.is_authenticated:
        user_cart= Cart.objects.get_or_create(user=request.user)
        cart_items = ProductCart.objects.filter(cart=user_cart)
        return render(request, 'cart.html', {'cart_items': cart_items})
    return redirect('login')  # Redirect to login page if not logged in

def product_details(request,product_id):
  
       
    return redirect('login')  # Redirect to login page if not logged in

def add_to_cart(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(pk=product_id)
        user_cart= Cart.objects.get_or_create(user=request.user)

        cart_item= ProductCart.objects.get_or_create(cart=user_cart, product=product)
        cart_item.quantity += 1
        cart_item.save()

        return redirect('product_list')
    return redirect('login')  # Redirect to login page if not logged in

def remove_from_cart(request, cart_item_id):
    if request.user.is_authenticated:
        cart_item = ProductCart.objects.get(pk=cart_item_id)
        if cart_item.cart.user == request.user:
            if cart_item.quantity > 1:
                cart_item.quantity -= 1
                cart_item.save()
            else:
                cart_item.delete()
        return redirect('cart_view')
    return redirect('login')  # Redirect to login page if not logged in

def checkout(request):
    if request.user.is_authenticated:
        user_cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = ProductCart.objects.filter(cart=user_cart)

        total_amount = sum(item.total_price() for item in cart_items)

        if request.method == 'POST':
            payment_type = request.POST.get('payment_type')
            payment = Payment.objects.create(cart=user_cart, payment_type=payment_type, amount=total_amount)
            cart_items.delete()  
            return render(request, 'payment_success.html', {'payment': payment})

        return render(request, 'checkout.html', {'cart_items': cart_items, 'total_amount': total_amount})
    return redirect('login')  

