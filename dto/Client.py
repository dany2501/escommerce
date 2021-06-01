from flask import Flask

class Client(dict):

    def __init__(self,name,email,token):
        self.__name = name
        self.__token = token
        self.__email = email
        dict.__init__(self,name=name,email=email,token=token)
        
    def getName(self):
        return self.__name
    
    def getEmail(self):
        return self.__email

    def getToken(self):
        return self.__token
