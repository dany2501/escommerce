import json

from flask.json import jsonify
from sqlalchemy.sql.elements import True_
from rest.controller.Controller import Controller
import jwt
from datetime import date, datetime
from entities.Client import ClientModel,Client
from entities.Person import Person,PersonModel
from entities.User import User,UserModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.SignUpRS import SignUpRS
from uuid import uuid4

class SignUpController(Controller):
    def __init__(self):
        super(SignUpController,self).__init__()

    
    def registerUser(self,email,password,name):
        url = self.getUrl()
        if email and password:
            bodyRS = SignUpRS(True)
            headerRS = HeaderRS()
            host = str(email.split('@')[1])
            alumno = "alumno.ipn.mx"
            guinda = "alumnoguinda.mx"
            if host == alumno or host == guinda:
                n = name.split(' ')
                if len(n)==3:
                    PersonModel(url).createPerson(n[0],n[1]+" "+n[2])
                else:
                    PersonModel(url).createPerson(n[0],n[1])
                person = PersonModel(url).getLastPersonCreated()
                UserModel(url).createUser(email,password,person.id)
                user = UserModel(url).getLastUserCreated()
                rand_token = str(uuid4())
                ClientModel(url).createClient(datetime.now(),rand_token,datetime.now(),user.id)
                bodyRS.setToken(rand_token)
                response = Response(headerRS,bodyRS)
                print(response)
                return response
                
            else:
                print("Email doesn't allowed")
        else:
            print("Data not provided")