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
from entities.Person import Cart, Person,PersonModel, ProductImage
from entities.Product import ProductModel
from entities.Cart import CartModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.CartRS import CartRS
from mappers.mapper import Mapper
from uuid import uuid4
class CartController(Controller):
    def __init__(self):
        super(CartController,self).__init__()

    def addProduct(self,token,productId,qty):
        if token is not None and productId is not None:
            bodyRS = CartRS(True)
            headerRS = HeaderRS()
            url = self.getUrl()
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId())
                if cart is None:
                    cart = CartModel(url).createCart(client[0].getId(),1,datetime.now())
                    cart = CartModel(url).getCartByClientId(client[0].getId())
                product = ProductModel(url).getProductById(productId)
                if product is not None:
                    CartModel(url).addProductToCart(cart.getId(),product.getId(),qty)
                    products = CartModel(url).getProductsCart(cart.getId())
                    if products is not None:
                        cartResponse =[]
                        for p in products:
                            image = ProductModel(url).getImageByProductId(p.getProductId())
                            cartResponse.append(Mapper().mapToCart(ProductModel(url).getProductById(p.getProductId()),p.getQty(),image.getUrl()))
                        bodyRS.setProducts(cartResponse)
                        return Response(headerRS,bodyRS)

    def getProducts(self,token):
        if token is not None:
            bodyRS = CartRS(True)
            headerRS = HeaderRS()
            url = self.getUrl()
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId())
                products = CartModel(url).getProductsCart(cart.getId())
                if products is not None:
                    cartResponse =[]
                    for p in products:
                        image = ProductModel(url).getImageByProductId(p.getProductId())
                        cartResponse.append(Mapper().mapToCart(ProductModel(url).getProductById(p.getProductId()),p.getQty(),image.getUrl()))
                    bodyRS.setProducts(cartResponse)
                    return Response(headerRS,bodyRS)

                    





