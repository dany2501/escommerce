from abc import ABC
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

class AbstractModel(ABC):
    def __init__(self,url):
        self.engine = create_engine(url)
        self.session = Session(self.engine)
        self.session.expire_on_commit=False

    def update(self):
        self.session.commit()

    def insert(self,obj):
        self.session.add(obj)
        self.session.commit()

    def delete(self,obj):
        self.session.delete(obj)
        self.session.commit()