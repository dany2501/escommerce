from flask_restful import Resource
from flask import request
from rest.controller.SignUpController import SignUpController
from rest.controller.Response import ResponseFactory

class SignUpResource(Resource):
    
    def post (self):
        params = request.get_json()
        email = params['email']
        password = params['password']
        confirmPass = params['confirmPass']
        name = params['name']
        lastName = params['lastName']
        secondLastName = params['secondLastName']
        if email and password and confirmPass and name:
            return ResponseFactory.toResponse(SignUpController().registerUser(email,password,confirmPass,name,lastName,apm=secondLastName))
        #print(params)"