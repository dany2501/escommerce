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
        params = request.get_json()
        if params is not None:
            if 'productId' in params:
                return ResponseFactory.toResponse(ProductController().getProduct(params['productId']))
            else:
                if 'categoryId' in params:
                    return ResponseFactory.toResponse(ProductController().getProductsByCategoryId(categoryId=params['categoryId']))
                else:
                    if  'name' in params:
                        return ResponseFactory.toResponse(ProductController().getProductByName(params['name']))