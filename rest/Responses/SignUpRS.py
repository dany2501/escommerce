
from cerberus.responses.BodyRS import BodyRS

class SignUpRS(BodyRS):
    
    __token = None

    def __init__(self,success,error=None):
        BodyRS.__init__(self,success,error)

    def setToken(self,token):
        self.__token=token
        self.update(token=token)