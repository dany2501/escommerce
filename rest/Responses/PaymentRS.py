from cerberus.responses.BodyRS import BodyRS

class PaymentRS(BodyRS):

    __payment = None
    __digits = None

    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setPayment(self,payment):
        self.__payment=payment
        self.update(payment=payment)

    def setLastDigits(self,digits):
        self.__digits=digits
        self.update(digits=digits)