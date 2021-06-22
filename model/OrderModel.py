from datetime import datetime
from model.AbstractModel import AbstractModel
from entities.entities import Order

class OrderModel(AbstractModel):

    def __init__(self, url):
        super(OrderModel,self).__init__(url)
        self.url=url

    def createOrder(self,cartId,addressId,paymentId):
        order = Order()
        order.setCartId(cartId)
        order.setStatusId(1)
        order.setAddresId(addressId)
        order.setPaymentId(paymentId)
        order.setDeliveryId(1)
        order.setOrderedAt(datetime.now())
        self.insert(order)
        return order

    def getOrder(self,cartId):
        order = self.session.query(Order).filter(Order.cart_id==cartId).first()
        print(order)
        return order