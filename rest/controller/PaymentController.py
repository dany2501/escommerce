from rest.controller.Controller import Controller
from model.ClientModel import ClientModel
from model.PaymentModel import PaymentModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.PaymentRS import PaymentRS
from mappers.mapper import Mapper
from cerberus.dtos.Error import Error
from rest.util.Cifrado import Cifrado


class PaymentController(Controller):
    def __init__(self):
        super(PaymentController, self).__init__()

    def registratePaymentMethod(self, payment, token):
        bodyRS = PaymentRS(True)
        headerRS = HeaderRS()

        if payment is not None:
            url = self.getUrl()
            if token is not None:
                client = ClientModel(url).getDataClient(token)
                if client is not None:
                    cardToken = Cifrado(self.getSecret()).encrypt(payment["cardNumber"])
                    if cardToken is not None:
                        end = payment["cardNumber"][-4:]
                        payment = PaymentModel(url).registerPayment(payment["cardHolder"],cardToken,payment["month"],payment["year"],payment["cvv"],client[0].getId())
                        if payment is not None:
                            bodyRS.setLastDigits(end)
                            return Response(headerRS, bodyRS)
                        else:
                            bodyRS = PaymentRS(False,Error(1003,"Error al guardar el método de pago."))
                            return Response(headerRS, bodyRS)
                    else:
                        bodyRS = PaymentRS(False,Error(1002,"Error al tokenizar la tarjeta"))
                        return Response(headerRS, bodyRS)
                else:
                    bodyRS = PaymentRS(False, Error(1001, "No se encontró al usuario"))
                    return Response(headerRS, bodyRS)
            else:
                bodyRS = PaymentRS(False, Error(1001, "No se encontró al usuario"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = PaymentRS(False, Error(1000, "No se encontraron datos para guardar"))
            return Response(headerRS, bodyRS)

    def getPaymentMethod(self, token):
        bodyRS = PaymentRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        client = ClientModel(url).getDataClient(token)
        if client is not None:
            payment = PaymentModel(url).getPayments(client[0].getId())
            if payment is not None:
                payments = []
                for p in payment:
                    card = Cifrado(self.getSecret()).decrypt(p.getToken())
                    payments.append(Mapper().mapToPayment(p,card,card[-4:]));
                bodyRS.setPayment(payments)
                return Response(headerRS, bodyRS)
            else:
                bodyRS = PaymentRS(False, Error(8002, "No hay métodos de pago"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = PaymentRS(False, Error(8001, "No se encontró al usuario"))
            return Response(headerRS, bodyRS)

    def deletePayment(self,token,paymentId):
        bodyRS = PaymentRS(True)
        url = self.getUrl()

        client = ClientModel(url).getDataClient(token)
        
        if client is None:
            bodyRS = PaymentRS(False,Error(1000, "No se encontró al usuario"))
            return Response(HeaderRS(),bodyRS)
        
        payment = PaymentModel(url).getPaymentById(paymentId)

        if payment is None:
            bodyRS = PaymentRS(False,Error(1000, "No se encontró el método de pago"))
            return Response(HeaderRS(),bodyRS)

        PaymentModel(url).deletePayment(paymentId)

        return Response(HeaderRS(),bodyRS)
        