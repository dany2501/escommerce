from flask_restful import Resource
from flask import request
from rest.controller.CartController import CartController
from rest.controller.Response import ResponseFactory
class CartResource(Resource):

    def get(self):
        headers = request.headers['token']
        if headers:
            return ResponseFactory.toResponse(CartController().getProducts(headers))
        #else:
           # print("Token not provided")
        #print(params)"

    def post(self):
        print("Request")
        headers = request.headers['token']
        params = request.form
        productId = params['productId']
        qty = params['qty']
        print(qty)
        return ResponseFactory.toResponse(CartController().addProduct(headers,productId,qty))