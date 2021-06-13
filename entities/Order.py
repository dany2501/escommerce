from datetime import datetime
from entities.AbstractModel import AbstractModel
from entities.Person import Order

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