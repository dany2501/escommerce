import json

from flask.json import jsonify
from requests.api import head
from sqlalchemy.sql.elements import True_
from rest.controller.Controller import Controller
import jwt
from datetime import date, datetime
from entities.Client import ClientModel,Client
from entities.Person import Person,PersonModel
from entities.User import User,UserModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.LoginRS import LoginRS
from mappers.mapper import Mapper
from uuid import uuid4
class LoginController(Controller):
    def __init__(self):
        super(LoginController,self).__init__()

    
    def loginUser(self,email,password):
        secret = self.getSecret()
        url = self.getUrl()
        if email and password:
            bodyRS = LoginRS(True)
            headerRS = HeaderRS()
            client = ClientModel(url).loginClient(email,password)
            if client is not None and client is not False:
                token = str(uuid4())
                session = ClientModel(url).updateClient(client[0].id,token,datetime.now())
                if session:
                    c = Mapper().mapToClient(client[2].getName()+" "+client[2].getLastName(),client[1].getEmail(),token)
                    bodyRS.setClient(c)
                    return Response(headerRS,bodyRS)
        else:
            print("Data not provided")

    def getDataClient(self,token):
        bodyRS = LoginRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        if token:
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                c = Mapper().mapToClient(client[2].getName()+" "+client[2].getLastName(),client[1].getEmail(),client[0].getToken())
                bodyRS.setClient(c)
                return Response(headerRS,bodyRS)

    def logOutUser(self,token):
        url = self.getUrl()
        bodyRS = LoginRS(True)
        headerRS = HeaderRS()

        if token:
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                return True
            else:
                return False