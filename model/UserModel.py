from entities.entities import Person
import hashlib
from model.AbstractModel import AbstractModel
from entities.entities import User


class UserModel(AbstractModel):

    def __init__(self, url):
        super(UserModel,self).__init__(url)
        self.url=url

    def createUser(self,email,password,person_id,code):
        user = User()
        user.setEmail(email)
        user.setPassword(self.encryptPassword(password))
        user.setPersonId(person_id)
        user.setCode(code)
        user.setStatusId(2)
        self.insert(user)
        return user

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

    def getUserByEmail(self,email):
        user = self.session.query(User).filter(User.email==email).first()
        if user is not None:
            return user
        else:
            return None

    def updateUserStatus(self,userId,statusId):
        user = self.session.query(User).filter(User.id==userId).update({"user_status_id":statusId})
        self.update()
        return user