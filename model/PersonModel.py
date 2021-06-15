from entities.entities import Person
from model.AbstractModel import AbstractModel
class PersonModel(AbstractModel):

    def __init__(self, url):
        super(PersonModel,self).__init__(url)
        self.url=url

    def createPerson(self,name,lastName,secondLastName):
        person = Person()
        person.setName(name)
        person.setLastName(lastName)
        person.setSecondLastName(secondLastName)
        self.insert(person)
        return person

    def updatePerson(self,personId,name,lastName):
        self.session.query(Person).filter(Person.id==personId).update({"name":name,"last_name":lastName})
        self.update()
        return [True,"Update successfully"]

    def getPerson(self,personId):
        person = self.session.query(Person).filter(Person.id==personId).first()
        if person is not None:
            return person
        else:
            print("Throw Exception")

    def deletePerson(self,personId):
        person = self.session.query(Person).filter(Person.id==personId).first()
        self.session.delete(person)
        self.session.commit()
        return [True,"User deleted successfully"]

    def getLastPersonCreated(self):
        person = self.session.query(Person).order_by(Person.id.desc()).first()
        if person is not None:
            return person
        else:
            print("Throw Exception")