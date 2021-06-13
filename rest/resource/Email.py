from flask_restful import Resource
from flask import request
from rest.controller.EmailController import EmailController
from rest.controller.Response import ResponseFactory


class EmailResource(Resource):
    def get(self):
        token = request.headers["token"]
        """if token:
            return ResponseFactory.toResponse(CartController().getProducts(token))"""
        # else:
        # print("Token not provided")
        # print(params)"

    def post(self):
        token = request.headers["token"]
        params = request.get_json()
        code = params["code"]
        email = params["email"]
        return ResponseFactory.toResponse(
            EmailController().validateEmail(token=token, code=code, email=email)
        )