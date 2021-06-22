from cerberus.responses.BodyRS import BodyRS

class OrderRS(BodyRS):
    
    __orderId = None
    __arrivalDate = None
    __orders = None


    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setOrderId(self,orderId):
        self.__orderId=orderId
        self.update(orderId=orderId)
   
    def setArrivalDate(self,arrivalDate):
        self.__arrivalDate=arrivalDate
        self.update(arrivalDate=arrivalDate)
    
    def setOrders(self,orders):
        self.__orders=orders
        self.update(orders=orders)