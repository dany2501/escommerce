from flask import Flask

class Order(dict):

    def __init__(self,id,qty,total,arrival):
        self.__id = id
        self.__qty = qty
        self.__total = total
        self.__arrival = arrival
        dict.__init__(self,id=id,qty=qty,total=total,arrival=arrival)
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__qty
    
    def getNumber(self):
        return self.__total
    
    def getDigits(self):
        return self.__arrival
