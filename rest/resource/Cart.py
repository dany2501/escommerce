from flask_restful import Resource
from flask import request
from rest.controller.CartController import CartController
from rest.controller.Response import ResponseFactory


class CartResource(Resource):
    def get(self):
        token = request.headers["token"]
        cartType = request.headers["cartType"]
        if token:
            return ResponseFactory.toResponse(CartController().getProducts(token,cartType))
        # else:
        # print("Token not provided")
        # print(params)"

    def post(self):
        token = request.headers["token"]
        params = request.get_json()
        print(params)
        cartType = params["cartType"]
        productId = params["productId"]
        qty = params["qty"]
        return ResponseFactory.toResponse(
            CartController().addProduct(token, productId, qty,cartType)
        )
    def put(self):
        token = request.headers["token"]
        params = request.get_json()
        productId = params["productId"]
        cartType = params["cartType"]
        return ResponseFactory.toResponse(
            CartController().deleteProduct(token, productId,cartType)
        )

    def delete(self):
        token = request.headers["token"]
        params = request.get_json()
        cartType = params["cartType"]
        return ResponseFactory.toResponse(CartController().deleteProducts(token,cartType))
