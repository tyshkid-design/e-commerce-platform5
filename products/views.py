from django.shortcuts import render, get_object_or_404
from .models import Product
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib import messages

def home(request):
    # Featured products: first 3 products
    featured_products = Product.objects.filter(is_featured=True)[:3]
    return render(request, 'products/home.html', {'featured_products': featured_products})

def shop(request):
    products = Product.objects.all()  # All products
    return render(request, 'products/shop.html', {'products': products})

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
