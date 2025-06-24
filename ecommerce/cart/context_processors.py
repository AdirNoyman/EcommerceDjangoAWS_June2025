from .cart import Cart

def cart(request):
    """
    Context processor to add the cart to the context.
    This allows us to access the cart in all templates.
    """
    return {'cart': Cart(request)}