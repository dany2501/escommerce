from re import I
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,DateTime,Boolean,ForeignKey,Float,Text,Time,DECIMAL
from entities.Person import Person
import hashlib
from entities.AbstractModel import AbstractModel
from entities.Person import User


class UserModel(AbstractModel):

    def __init__(self, url):
        super(UserModel,self).__init__(url)
        self.url=url

    def createUser(self,email,password,person_id):
        user = User()
        user.setEmail(email)
        user.setPassword(self.encryptPassword(password))
        user.setPersonId(person_id)
        self.insert(user)

    def updateUser(self,userId,email,password):
        self.session.query(User).filter(User.id==userId).update({"email":email,"password":password})
        self.update

    def deleteUser(self,userId):
        user = self.session.query(User).filter(User.id==userId).first()
        self.session.delete(user)
        self.session.commit()

    def encryptPassword(self,password):
        hashed = hashlib.sha512(password.encode())
        return hashed.hexdigest()

    
    def getUserData(self,userId):
        user = self.session.query(User).filter(User.id==userId).first()
        userData = self.session.query(Person).filter(Person.id==user.getPersonId()).first()
        if userData is not None:
            return userData
        else:
            print("Throw Exception")

    def getLastUserCreated(self):
        user = self.session.query(User).order_by(User.id.desc()).first()
        if user is not None:
            return user
        else:
            print("Throw Exceptio")
