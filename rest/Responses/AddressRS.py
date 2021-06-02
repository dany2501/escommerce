from cerberus.responses.BodyRS import BodyRS

class AddressRS(BodyRS):

    __address = None

    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setAddress(self,address):
        self.__address=address
        self.update(address=address)