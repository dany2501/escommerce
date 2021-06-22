from entities.entities import Colonia
from model.AbstractModel import AbstractModel


class ZipCodeModel(AbstractModel):

    def __init__(self, url):
        super(ZipCodeModel,self).__init__(url)
        self.url=url


    def findZipCode(self,zipcode):
        code = self.session.query(Colonia).filter(Colonia.zipcode==zipcode).first()
        if code is not None:
            return code
        else:
            return None