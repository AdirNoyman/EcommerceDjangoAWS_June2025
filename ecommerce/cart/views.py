from django.shortcuts import render

def cart_summary(request):
    return render(request, "cart/cart-summary.html")

def cart_add(request, product_id):
    # Logic to add product to cart
    return render(request, "cart/cart-add.html", {"product_id": product_id})

def cart_update(request, product_id):
    # Logic to update product quantity in cart
    return render(request, "cart/cart-update.html", {"product_id": product_id})

def cart_delete(request, product_id):
    # Logic to delete product from cart
    return render(request, "cart/cart-delete.html", {"product_id": product_id})

