

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