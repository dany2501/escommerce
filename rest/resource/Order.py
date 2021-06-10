from flask_restful import Resource
from flask import request
from rest.controller.OrderController import OrderController
from rest.controller.Response import ResponseFactory
class OrderResource(Resource):

    def get(self):
        #headers = request.headers['token']
        #if headers:
        print("")
        #categoryId = request.headers['categoryId']
        #return ResponseFactory.toResponse(ProductController().getProducts(categoryId=categoryId))
        #else:
           # print("Token not provided")
        #print(params)"

    def post(self):
        token = request.headers['token']
        params = request.form
        paymentId = params['paymentId']
        addressId = params['addressId']
        return ResponseFactory.toResponse(OrderController().createOrder(token,addressId,paymentId))