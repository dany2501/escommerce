from entities.Product import ProductModel
from entities.Cart import CartModel
import json

from flask.json import jsonify
from requests.api import head
from sqlalchemy.sql.elements import True_
from rest.controller.Controller import Controller
import jwt
from datetime import date, datetime
from entities.Client import ClientModel,Client
from entities.Product import ProductModel
from entities.Address import AddressModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.AddressRS import AddressRS
from mappers.mapper import Mapper
from uuid import uuid4

class AddressController(Controller):
    def __init__(self):
        super(AddressController,self).__init__()

    def createAddress(self,address,token):
        bodyRS = AddressRS(True)
        headerRS = HeaderRS()

        if address is not None:
            url = self.getUrl()
            if token is not None:
                client = ClientModel(url).getDataClient(token)
                if client is not None:
                    AddressModel(url).createAddress(address['name'],address['street'],address['extNum'],address['zipCode'],address['suburb'],address['city'],address['phone'],client[0].getId())
                address = AddressModel(url).getAddressByClientId(client[0].getId())
                if address is not None:
                    return Response(headerRS,bodyRS)
    
    def getAddress(self,token):
        bodyRS = AddressRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        client = ClientModel(url).getDataClient(token)
        if client is not None:
            address = AddressModel(url).getAddressByClientId(client[0].getId())
            if address is not None:
                bodyRS.setAddress(Mapper().mapToAddress(address))
                return Response(headerRS,bodyRS)


