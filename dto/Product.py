from flask import Flask

class Product(dict):

    def __init__(self,id,name,description,price,sku,stock,categoryId,image):
        self.__id = id
        self.__name = name
        self.__description = description
        self.__price = price
        self.__sku = sku
        self.__stock = stock
        self.__categoryId = categoryId
        self.__image = image
        dict.__init__(self,id=id,name=name,description=description,price=price,sku=sku,stock=stock,categoryId=categoryId,image=image)
        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description

    def getPrice(self):
        return self.__price

    def getSku(self):
        return self.__sku

    def getStock(self):
        return self.__stock

    def getCategoryId(self):
        return self.__categoryId

    def getImage(self):
        return self.__image
