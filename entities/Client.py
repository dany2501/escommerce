from re import I
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,DateTime,Boolean,ForeignKey,Float,Text,Time,DECIMAL
from sqlalchemy.sql.sqltypes import CLOB
from entities.User import User
import hashlib
from entities.AbstractModel import AbstractModel
Base = declarative_base()
from entities.Person import Client,User,Person

class ClientModel(AbstractModel):

    def __init__(self, url):
        super(ClientModel,self).__init__(url)
        self.url=url

    def createClient(self,registrationDate,token,lastLogin,idUser):
        client = Client()
        client.setRegistrationDate(registrationDate)
        client.setToken(token)
        client.setLastLogin(lastLogin)
        client.setIdUser(idUser)
        self.insert(client)

    def updateClient(self,clientId,token,lastLogin):
        self.session.query(Client).filter(Client.id==clientId).update({"token":token,"last_login":lastLogin})
        self.session.commit()
        return True

    def deleteClient(self,clientId):
        client = self.session.query(Client).filter(Client.id==clientId).first()
        self.session.delete(client)
        self.session.commit()

    def encryptPassword(self,password):
        hashed = hashlib.sha512(password.encode())
        return hashed.hexdigest()

    def loginClient(self,email,password):
        hpass = self.encryptPassword(password)
        client = self.session.query(Client,User,Person).select_from(User).join(Client).join(Person).filter(User.email==email,User.password==hpass).first()
        if client is not None:
            return client
        else:
            return False

    def getDataClient(self,token):
        data = self.session.query(Client,User,Person).select_from(Client).join(User).join(Person).filter(Client.token==token).first()
        if data is not None:
            return data