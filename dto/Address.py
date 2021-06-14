from flask import Flask

class Address(dict):

    def __init__(self,name,lastName,street,extNum,city,suburb,zipCode,phone,id):
        self.__id=id
        self.__name = name
        self.__lastName = lastName
        self.__street = street
        self.__extNum = extNum
        self.__city= city
        self.__suburb = suburb
        self.__zipCode = zipCode
        self.__phone = phone
        dict.__init__(self,name=name,lastName=lastName,street=street,extNum=extNum,city=city,suburb=suburb,zipCode=zipCode,phone=phone,id=id)
        
    def getId(self):
        return self.__id

    def getName(self):
        return self.__name
    
    def getLastName(self):
        return self.__lastName
    
    def getStreet(self):
        return self.__street
    
    def getExtNum(self):
        return self.__extNum
    
    def getCity(self):
        return self.__city
    
    def getSuburb(self):
        return self.__suburb
    
    def getZipCode(self):
        return self.__zipCode
    
    def getPhone(self):
        return self.__phone
