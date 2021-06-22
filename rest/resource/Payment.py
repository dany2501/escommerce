from flask_restful import Resource
from flask import request
from rest.controller.PaymentController import PaymentController
from rest.controller.Response import ResponseFactory

class PaymentResource(Resource):

    def get(self):
        headers = request.headers['token']
        return ResponseFactory.toResponse(PaymentController().getPaymentMethod(headers))

    def post(self):
        token = request.headers['token']
        params = request.get_json()
        payment = params['payment']
        return ResponseFactory.toResponse(PaymentController().registratePaymentMethod(payment,token))

    def delete(self):
        token = request.headers['token']
        params = request.get_json()
        paymentId = params['paymentId']

        return ResponseFactory.toResponse(PaymentController().deletePayment(token,paymentId))