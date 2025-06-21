from django.shortcuts import render
from . models import Category, Product

# Create your views here.
def store(request):
    all_products = Product.objects.all()
    context = {
        'products': all_products,
    }
    return render(request, 'store/store.html', context)

def categories(request):
    all_categories = Category.objects.all()    
    return {'categories': all_categories}
