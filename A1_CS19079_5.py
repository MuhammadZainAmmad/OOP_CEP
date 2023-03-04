class Cart:
    def __init__(self):
        self.cart = []

    def currentCart(self):  # return current cart
        return self.cart

    def addToCart(self, product):  # add a product to cart
        self.cart.append(product)
        return self.cart

    def removeFromCart(self, product):  # remove product from cart
        for i in self.cart:
            if i == product:
                self.cart.remove(i)
        return self.cart

    def emptyCart(self):  # Empty the cart
        self.cart = []
        return self.cart


# a = Cart()
# print(a.currentCart())
# print(a.addToCart('a'))
# print(a.addToCart('b'))
# print(a.addToCart('c'))
# print(a.currentCart())
# print(a.removeFromCart('c'))
# print(a.emptyCart())