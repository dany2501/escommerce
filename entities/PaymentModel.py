from dto.Payment import Payment
from sqlalchemy import or_
from entities.AbstractModel import AbstractModel
from entities.Person import PaymentMethod

class PaymentModel(AbstractModel):

    def __init__(self, url):
        super(PaymentModel,self).__init__(url)
        self.url=url

    def registerPayment(self,cardholder,cardNumber,monthExpiration,yearExpiration,cvv,clientId):
        payment = PaymentMethod()
        payment.setCardholder(cardholder)
        payment.setToken(cardNumber)
        payment.setMonthExpiration(monthExpiration)
        payment.setYearExpiration(yearExpiration)
        payment.setCvv(cvv)
        payment.setClientId(clientId)
        self.insert(payment)
        return payment

    def getLastPayment(self,clientId):
        payment = self.session.query(PaymentMethod).filter(PaymentMethod.client_id==clientId).order_by(PaymentMethod.id.desc()).first()
        if payment is not None:
            return payment
        else:
            return None

    def getPaymentById(self,paymentId):
        payment = self.session.query(PaymentMethod).filter(PaymentMethod.id==paymentId).first()
        if payment is not None:
            return payment
        else:
            return None