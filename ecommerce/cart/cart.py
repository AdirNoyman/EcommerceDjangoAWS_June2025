

class Cart():
    def __init__(self, request):
        self.session = request.session
        # Returning user - obtaining his current session
        cart = self.session.get('session_key')
        print (f"Current cart: {cart}")

        # New user - generating a new session (dict with session_key, key)
        if not cart:
            cart = self.session['session_key'] = {}
            print(f"Created new cart: {cart}")

        # If the user already has a cart, we use it, else the cart will be empty dict
        self.cart = cart
    
    def add(self, product, product_qty):
        """
        Add product to the cart or update its quantity if it already exists.
        """
        product_id = str(product.id)
        if product_id in self.cart:
            self.cart[product_id]['qty'] += product_qty
        else:
            self.cart[product_id] = {'qty': product_qty, 'price': str(product.price)}
        # Mark the session as modified to ensure it is saved
        self.session.modified = True