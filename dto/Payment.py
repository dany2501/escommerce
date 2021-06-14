from flask import Flask

class Payment(dict):

    def __init__(self,id,name,number,digits,year,month,cvv):
        self.__id = id
        self.__name = name
        self.__number = number
        self.__digits = digits
        self.__year = year
        self.__month = month
        self.__cvv = cvv
        dict.__init__(self,id=id,name=name,number=number,digits=digits,year=year,month=month,cvv=cvv)
    
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getNumber(self):
        return self.__number
    
    def getDigits(self):
        return self.__digits

    def getYear(self):
        return self.__year

    def getMonth(self):
        return self.__month
    
    def getCvv(self):
        return self.__cvv