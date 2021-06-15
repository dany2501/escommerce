from entities.entities import User
import hashlib
from model.AbstractModel import AbstractModel
from entities.entities import Client,User,Person

class ClientModel(AbstractModel):

    def __init__(self, url):
        super(ClientModel,self).__init__(url)
        self.url=url

    def createClient(self,registrationDate,token,lastLogin,idUser):
        client = Client()
        client.setRegistrationDate(registrationDate)
        client.setToken(token)
        client.setLastLogin(lastLogin)
        client.setIdUser(idUser)
        self.insert(client)
        return client

    def updateClient(self,clientId,token,lastLogin):
        self.session.query(Client).filter(Client.id==clientId).update({"token":token,"last_login":lastLogin})
        self.session.commit()
        self.session.close()
        return True

    def deleteClient(self,clientId):
        client = self.session.query(Client).filter(Client.id==clientId).first()
        self.session.close()
        self.session.delete(client)
        self.session.commit()

    def encryptPassword(self,password):
        hashed = hashlib.sha512(password.encode())
        return hashed.hexdigest()

    def getClientByEmail(self,email):
        client = self.session.query(User).select_from(User).filter(User.email==email).first()
        self.session.close()
        if client is not None:
            return client
        else:
            return None

    def getClientByEmailCode(self,email):
        client = self.session.query(Client,User).select_from(User).join(Client).filter(User.email==email).first()
        self.session.close()
        if client is not None:
            return client
        else:
            return None


    def loginClient(self,email,password):
        hpass = self.encryptPassword(password)
        client = self.session.query(Client,User,Person).select_from(User).join(Client).join(Person).filter(User.email==email,User.password==hpass).first()
        if client is not None:
            self.session.close()
            return client
        else:
            return None

    def getDataClient(self,token):
        data = self.session.query(Client,User,Person).select_from(Client).join(User).join(Person).filter(Client.token==token).first()
        self.session.close()
        if data is not None:
            return data
        