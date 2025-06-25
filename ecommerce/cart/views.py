from django.shortcuts import render
from .cart import Cart
from store.models import Product
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

def cart_summary(request):
    return render(request, "cart/cart-summary.html")

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_quantity = int(request.POST.get('product_quantity'))
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, product_qty=product_quantity)
        return JsonResponse({"Product name": product.title, "Product quantity": product_quantity}, status=200)

def cart_update(request, product_id):
    # Logic to update product quantity in cart
    return render(request, "cart/cart-update.html", {"product_id": product_id})

def cart_delete(request, product_id):
    # Logic to delete product from cart
    return render(request, "cart/cart-delete.html", {"product_id": product_id})

