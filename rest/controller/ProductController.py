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
from entities.Product import ProductModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.ProductsRS import ProductsRS
from mappers.mapper import Mapper
from uuid import uuid4
class ProductController(Controller):
    def __init__(self):
        super(ProductController,self).__init__()

    def getProducts(self):
        #if token is not None:
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()

        url = self.getUrl()
        #client = ClientModel(url).getDataClient(token)
        #if client is not None:
        products = ProductModel(url).getProducts()
        if products is not None:
            productList=[]
            for product in products:
                image = ProductModel(url).getImageByProductId(product.getId())
                productList.append(Mapper().mapToProduct(product,image.getUrl()))
            bodyRS.setProducts(productList)
            return Response(headerRS,bodyRS)
                    
    def getProduct(self,productId):
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()

        url = self.getUrl()

        if productId is not None:
            print(productId)
            product = ProductModel(url).getProductById(productId)
            image = ProductModel(url).getImageByProductId(product.getId())
            if product is not None:
                bodyRS.setProducts(Mapper().mapToProduct(product,image.getUrl()))
                return Response(headerRS,bodyRS)

    