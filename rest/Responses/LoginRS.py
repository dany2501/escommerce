
from cerberus.responses.BodyRS import BodyRS

class LoginRS(BodyRS):
    
    __client = None

    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setClient(self,client):
        self.__client=client
        self.update(client=client)