from datetime import date, datetime
from entities.AbstractModel import AbstractModel
from entities.Person import Cart,CartProduct

class CartModel(AbstractModel):

    def __init__(self, url):
        super(CartModel,self).__init__(url)
        self.url=url

    def createCart(self,clientId,statusId,createdAt):
        cart = Cart()
        cart.setClientId(clientId)
        cart.setStatusId(statusId)
        cart.setCreatedAt(createdAt)
        cart.setUpdatedAt(createdAt)
        self.insert(cart)
        return cart

    def getCartByClientId(self,clientId):
        cart = self.session.query(Cart).filter(Cart.client_id==clientId,Cart.status_id==1).first()
        if cart is not None:
            return cart
        else:
            return None

    def addProductToCart(self,cartId,productId,qty):
        product = self.session.query(CartProduct).filter(CartProduct.cart_id==cartId,CartProduct.product_id==productId).first()
        if product is not None:
            self.session.query(Cart).filter(Cart.id==cartId).update({"updated_at":datetime.now()})
            self.session.query(CartProduct).filter(CartProduct.cart_id==cartId,CartProduct.product_id==productId).update({"qty":qty})
            self.update()
        else:
            cart = CartProduct()
            cart.setCartId(cartId)
            cart.setProductId(productId)
            cart.setQty(qty)
            self.insert(cart)

    def getProductsCart(self,cartId):
        cart = self.session.query(CartProduct).filter(CartProduct.cart_id==cartId).all()
        if cart is not None:
            return cart
        else:
            return None

    def deleteProducts(self,cartId):
        cart = self.session.query(CartProduct).filter(CartProduct.cart_id==cartId).all()
        if cart is not None:
            for product in cart:
                self.delete(product)
            return True

    def deleteProductById(self,cartId,productId):
        product = self.session.query(CartProduct).filter(CartProduct.cart_id==cartId,CartProduct.product_id==productId).first()
        if product is not None:
            self.delete(product)
            return True

    def cartOrdered(self,cartId):
        self.session.query(Cart).filter(Cart.id==cartId).update({"updated_at":datetime.now(),"status_id":2})
        self.update()
        return True
