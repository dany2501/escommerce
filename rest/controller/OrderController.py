from datetime import date, datetime, timedelta
from entities.PaymentModel import PaymentModel
from entities.Client import ClientModel
from entities.Order import OrderModel
from entities.Cart import CartModel
from entities.Address import AddressModel
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

    def createOrder(self,token,addressId,paymentId):
        url = self.getUrl()
        headerRS = HeaderRS()
        if token is not None:
            bodyRS = OrderRS(True)
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId())

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
                    cart.setOrderedAt(datetime.now())
                    CartModel(url).cartOrdered(cart.getId())
                    bodyRS.setOrderId(order.getId())
                    bodyRS.setArrivalDate(str(order.getOrderedAt()+timedelta(3)))
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

                
