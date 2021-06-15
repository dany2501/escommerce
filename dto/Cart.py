from flask import Flask

class Cart(dict):

    def __init__(self,product,qty):
        self.__product = product
        self.__qty = qty
        dict.__init__(self,product=product,qty=qty)
        
    def getProduct(self):
        return self.__product
    
    def getQty(self):
        return self.__qty
