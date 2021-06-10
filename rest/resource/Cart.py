from flask_restful import Resource
from flask import request
from rest.controller.CartController import CartController
from rest.controller.Response import ResponseFactory


class CartResource(Resource):
    def get(self):
        token = request.headers["token"]
        if token:
            return ResponseFactory.toResponse(CartController().getProducts(token))
        # else:
        # print("Token not provided")
        # print(params)"

    def post(self):
        token = request.headers["token"]
        params = request.form
        productId = params["productId"]
        qty = params["qty"]
        return ResponseFactory.toResponse(
            CartController().addProduct(token, productId, qty)
        )
    def put(self):
        token = request.headers["token"]
        params = request.form
        productId = params["productId"]
        return ResponseFactory.toResponse(
            CartController().deleteProduct(token, productId)
        )

    def delete(self):
        token = request.headers["token"]
        return ResponseFactory.toResponse(CartController().deleteProducts(token))
