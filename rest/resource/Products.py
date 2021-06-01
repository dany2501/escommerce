from flask_restful import Resource
from flask import request
from rest.controller.ProductController import ProductController
from rest.controller.Response import ResponseFactory
class ProductsResource(Resource):

    def get(self):
        #headers = request.headers['token']
        #if headers:
        return ResponseFactory.toResponse(ProductController().getProducts())
        #else:
           # print("Token not provided")
        #print(params)"

    def post(self):
        params = request.form
        productId = params['productId']
        return ResponseFactory.toResponse(ProductController().getProduct(productId))