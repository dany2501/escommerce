from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,DateTime,Boolean,ForeignKey,Float,Text,Time,DECIMAL
from sqlalchemy.sql.sqltypes import CLOB
from entities.User import User
import hashlib
from entities.AbstractModel import AbstractModel
Base = declarative_base()
from entities.Person import Address

class AddressModel(AbstractModel):
    def __init__(self, url):
        super(AddressModel,self).__init__(url)
        self.url=url

    def createAddress(self,name,street,extNumber,zipCode,suburb,city,phone,clientId):
        address = Address()
        address.setName(name)
        address.setStreet(street)
        address.setExtNumber(extNumber)
        address.setZipCode(zipCode)
        address.setSuburb(suburb)
        address.setCity(city)
        address.setPhone(phone)
        address.setClientId(clientId)
        self.insert(address)

    def getAddressByClientId(self,clientId):
        address = self.session.query(Address).filter(Address.client_id==clientId).order_by(Address.id.desc()).first()
        if address is not None:
            return address
        else:
            return None
    
    def getAddressById(self,id):
        address = self.session.query(Address).filter(Address.id==id).first()
        if address is not None:
            return address
        else:
            return None
