from flask_restful import Resource
from flask import request
from rest.controller.LoginController import LoginController
from rest.controller.Response import ResponseFactory
class LoginResource(Resource):
    def post (self):
        params = request.get_json()
        email = params['email']
        password = params['password']
        if email and password:
            return ResponseFactory.toResponse(LoginController().loginUser(email,password))

    def get(self):
        headers = request.headers['token']
        if headers:
            return ResponseFactory.toResponse(LoginController().getDataClient(headers))