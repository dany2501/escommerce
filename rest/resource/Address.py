from flask_restful import Resource
from flask import request
from rest.controller.AddressController import AddressController
from rest.controller.Response import ResponseFactory
class AddressResource(Resource):

    def get(self):
        headers = request.headers['token']
        if headers:
            return ResponseFactory.toResponse(AddressController().getAddress(headers))
        #else:
           # print("Token not provided")
        #print(params)

    def post(self):
        headers = request.headers['token']
        params = request.get_json()
        if params is not None:
            return ResponseFactory.toResponse(AddressController().createAddress(params,headers))