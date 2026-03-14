from django.shortcuts import render, get_object_or_404

import products
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Product
from django.contrib import messages
from django.shortcuts import redirect
from django.http import JsonResponse
from .models import Product,Artist


@login_required
def home(request):
    # Featured products: first 3 products
    featured_products = Product.objects.filter(is_featured=True)[:3]
    return render(request, 'products/home.html', {'featured_products': featured_products})

def shop(request):
    query = request.GET.get('q')

    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()

    return render(request, 'products/product_list.html', {'products': products})

def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'products/product_detail.html', {'product': product})

def signup_view(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user =form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'products/signup.html', {'form': form})


def add_to_cart(request, product_id):
    cart = request.session.get('cart', {})
    product_id = str(product_id)
    cart[product_id] = cart.get(product_id, 0) + 1
    request.session['cart'] = cart
    total_items = sum(cart.values())

    # Check if request is AJAX (from JS fetch)
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'message': 'Added to cart!', 'total_items': total_items})

    # Fallback for normal requests
    return redirect('shop')

def cart(request):
    cart = request.session.get('cart',{})
    cart_items = []
    total = 0
    
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product,id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })
        
    context = {
        'cart_items':cart_items,
        'total':total
    }    
    return render(request, 'products/cart.html',context)
    
    

# Remove from cart
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        request.session['cart'] = cart
    return redirect('cart')

# Update quantity
def update_cart(request, product_id):
    cart = request.session.get('cart', {})
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart[str(product_id)] = quantity
    else:
        cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

def cart_total(cart_items):
    return sum(item['product'].price * item['quantity'] for item in cart_items)

def cart_items_count(request):
    cart = request.session.get('cart', {})
    total_item= sum(int(quantity) for quantity in 
                    cart.values()) if cart else 0
    return {'cart_items_count': total_item}

def product_list(request):
    products = Product.objects.all()
    return render(request, 'products/product_list.html', {'products': products})

def checkout(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = Product.objects.get(id=product_id)
        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    context = {
        'cart_items': cart_items,
        'total': total
    }

    return render(request, 'products/checkout.html', context)

def artist_profile(request, artist_id):
    artist = Artist.objects.get(id=artist_id)
    products = Product.objects.filter(artist=artist)
    return render(request, 'products/artist_profile.html', {
        'artist': artist,
        'products': products
    })