from datetime import date, datetime, timedelta
from dto.Cart import Cart
from dto.Order import Order
from model.ProductModel import ProductModel
from model.PaymentModel import PaymentModel
from model.ClientModel import ClientModel
from model.OrderModel import OrderModel
from model.CartModel import CartModel
from model.AddressModel import AddressModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.OrderRS import OrderRS
from mappers.mapper import Mapper
from uuid import uuid4
from rest.controller.Controller import Controller
from cerberus.dtos.Error import Error

class OrderController(Controller):
    def __init__(self):
        super(OrderController,self).__init__()

    def createOrder(self,token,addressId,paymentId,cartType):
        url = self.getUrl()
        headerRS = HeaderRS()
        if token is not None:
            bodyRS = OrderRS(True)
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId(),cartType)

                if cart is None:
                    bodyRS = OrderRS(False,Error(8000,"Ocurrió un error, intenta más tarde."))
                    return Response(headerRS,bodyRS)
                    
                address = AddressModel(url).getAddressById(addressId)
                if address is None:
                    bodyRS = OrderRS(False,Error(8005,"Ocurrió un error con la dirección de envío, intenta más tarde."))
                    return Response(headerRS,bodyRS)
                    
                payment = PaymentModel(url).getPaymentById(paymentId)
                if payment is None:
                    bodyRS = OrderRS(False,Error(8004,"Ocurrió un error con el método de pago, intenta más tarde."))
                    return Response(headerRS,bodyRS)

                
                order = OrderModel(url).createOrder(cart.getId(),address.getId(),payment.getId())
                if order is not None:

                    CartModel(url).cartOrdered(cart.getId())
                    products = CartModel(url).getProductsCart(cart.getId())
                    
                    for product in products:
                        ProductModel(url).updateStock(product.getQty(),product.getId())

                    cart.setOrderedAt(datetime.now())
                    bodyRS.setOrderId(order.getId())
                    date = order.getOrderedAt()+timedelta(3)
                    bodyRS.setArrivalDate(str(date.strftime('%Y-%m-%d')))
                    return Response(headerRS,bodyRS)
                    
                else:
                    bodyRS = OrderRS(False,Error(8000,"Ocurrió un error, intenta más tarde."))
                    return Response(headerRS,bodyRS)

            else:
                bodyRS = OrderRS(False,Error(8001,"No se encontró al cliente."))
                return Response(headerRS,bodyRS)
        else:
            bodyRS = OrderRS(False,Error(8002,"Credenciales inválidas"))
            return Response(headerRS,bodyRS)

    def getOrders(self,token):
        url = self.getUrl()
        headerRS = HeaderRS()
        if token is not None:
            bodyRS = OrderRS(True)
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                carts = CartModel(url).getOrders(client[0].getId())
                ordersList=[]
                for cart in carts:
                    order = OrderModel(url).getOrder(cart.getId())
                    date = order.getOrderedAt()+timedelta(3)
                    products = CartModel(url).getProductsCart(cart.getId())
                    price=0
                    prods =0
                    for product in products:
                        prods = prods+product.getQty()
                        p = ProductModel(url).getProductById(product.getProductId())
                        if p is not None:
                            price = price+p.getPrice()
                    ordersList.append(Order(order.getId(),prods,int(price),date.strftime('%Y-%m-%d')))
                bodyRS.setOrders(ordersList)
                return Response(headerRS,bodyRS)

                """for cart in carts:
                    cart.setOrderedAt(datetime.now())
                    bodyRS.setOrderId(order.getId())
                    date = order.getOrderedAt()+timedelta(3).strftime('%Y-%m-%d')
                    bodyRS.setArrivalDate(str(date))
                    return Response(headerRS,bodyRS)"""



                
