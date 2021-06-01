from cerberus.responses.BodyRS import BodyRS

class CartRS(BodyRS):
    
    __products = None

    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setProducts(self,products):
        self.__products=products
        self.update(products=products)