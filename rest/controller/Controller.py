from abc import ABC
from app import app
class Controller(ABC):
    def __init__(self):
        self.url = ""
        self.context ="escommerce_db"
        self.dbConnect = app.config.ESCOMMERCE_POOL_CONNECT
        self.secret = app.config.SECRET_ENCRYPT
    
    def getUrl(self):
        pool = self.dbConnect
        for item in pool:
            if item['context'] == self.context:
                self.url = item['database_uri']
        return self.url

    def getSecret(self):
        secret = self.secret
        return secret
    