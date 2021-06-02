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

class OrderController(Controller):
    def __init__(self):
        super(OrderController,self).__init__()

    def createOrder(token,data):
        url = self.getUrl()
        if token is not None and data is not None:
            client = ClientModel(url).getDataClient(token)
            