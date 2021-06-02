from decimal import Decimal
from flask import Flask
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer,Column,String,DateTime,Boolean,ForeignKey,Float,Text,Time,DECIMAL
from sqlalchemy.sql.expression import update
from sqlalchemy.sql.sqltypes import Date
from entities.AbstractModel import AbstractModel
Base = declarative_base()

class Person(Base):
    __tablename__='esc_person'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50),nullable=False)
    last_name = Column(String(50),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name
    
    def getLastName(self):
        return self.last_name

    def setLastName(self,last_name):
        self.last_name=last_name

class User(Base):
    __tablename__='esc_user'
    id = Column(Integer,primary_key=True,autoincrement=True)
    email = Column(String(100),nullable=False)
    password = Column(String(50),nullable=False)
    person_id = Column(Integer,ForeignKey('esc_person.id'),nullable=True)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def getEmail(self):
        return self.email
    
    def setEmail(self,email):
        self.email=email
    
    def getPassword(self):
        return self.password

    def setPassword(self,password):
        self.password=password
    
    def getPersonId(self):
        return self.person_id
    
    def setPersonId(self,person_id):
        self.person_id=person_id

class Client(Base):
    __tablename__='esc_client'
    id = Column(Integer,primary_key=True,autoincrement=True)
    registration_date = Column(DateTime,nullable=False)
    token = Column(String(50),nullable=True)
    last_login = Column(DateTime,nullable=True)
    user_id = Column(Integer,ForeignKey('esc_user.id'),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id
    
    def getRegistrationDate(self):
        return self.registration_date
    
    def setRegistrationDate(self,date):
        self.registration_date=date
    
    def getToken(self):
        return self.token

    def setToken(self,token):
        self.token=token
    
    def getLastLogin(self):
        return self.last_login
    
    def setLastLogin(self,last_login):
        self.last_login=last_login

    def getIdUser(self):
        return self.user_id
    
    def setIdUser(self,userId):
        self.user_id=userId

class Product(Base):
    __tablename__ = "esc_product"
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(100),nullable=False)
    description = Column(String(300),nullable=False)
    price = Column(DECIMAL,nullable=False)
    sku = Column(String(12),nullable=False)
    stock = Column(Integer,nullable=False)
    category_id = Column(Integer,nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name = name
    
    def getDescription(self):
        return self.description
    
    def setDescription(self,description):
        self.description = description
    
    def getPrice(self):
        return self.price
    
    def setPrice(self,price):
        self.price = price
    
    def getSku(self):
        return self.sku
    
    def setSku(self,sku):
        self.sku = sku
    
    def getStock(self):
        return self.stock
    
    def setStock(self,stock):
        self.stock = stock

    def getCategoryId(self):
        return self.category_id
    
    def setCategoryId(self,category_id):
        self.category_id = category_id

class Cart(Base):
    __tablename__ = "esc_cart"
    id = Column(Integer,primary_key=True,autoincrement=True)
    client_id = Column(Integer,ForeignKey('esc_client.id'),nullable=False)
    status_id = Column(Integer,ForeignKey('esc_status_cart.id'),nullable=False)
    created_at = Column(DateTime,nullable=False)
    updated_at = Column(DateTime,nullable=False)
    ordered_at = Column(DateTime,nullable=True)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getClientId(self):
        return self.client_id
    
    def setClientId(self,clientId):
        self.client_id=clientId
    
    def getStatusId(self):
        return self.status_id
    
    def setStatusId(self,statusId):
        self.status_id=statusId

    def getCreatedAt(self):
        return self.created_at
    
    def setCreatedAt(self,createdAt):
        self.created_at=createdAt

    def getUpdatedAt(self):
        return self.updated_at

    def setUpdatedAt(self,updatedAt):
        self.updated_at=updatedAt

    def getOrderedAt(self):
        return self.ordered_at
    
    def setOrderedAt(self,orderedAt):
        self.ordered_at=orderedAt

class CartProduct(Base):
    __tablename__ = "esc_cart_product"
    id = Column(Integer,primary_key=True,autoincrement=True)
    cart_id = Column(Integer,ForeignKey('esc_cart.id'),nullable=False)
    product_id = Column(Integer,ForeignKey('esc_product.id'),nullable=False)
    qty = Column(Integer,nullable=True)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getCartId(self):
        return self.cart_id
    
    def setCartId(self,cartId):
        self.cart_id=cartId
    
    def getProductId(self):
        return self.product_id
    
    def setProductId(self,product_id):
        self.product_id=product_id

    def getQty(self):
        return self.qty

    def setQty(self,qty):
        self.qty=qty

class StatusCart(Base):
    __tablename__ = "esc_status_cart"
    id = Column(Integer,primary_key=True,autoincrement=True)
    status = Column(String(45),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getStatus(self):
        return self.status
    
    def setStatus(self,status):
        self.status=status

class ProductImage(Base):
    __tablename__ = "esc_product_image"
    id = Column(Integer,primary_key=True,autoincrement=True)
    url = Column(String(100),nullable=False)
    product_id = Column(Integer,ForeignKey('esc_product.id'),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getUrl(self):
        return self.url
    
    def setUrl(self,url):
        self.url=url

    def getProductId(self):
        return self.product_id
    
    def setProductId(self,productId):
        self.product_id=productId

class Address(Base):
    __tablename__ = "esc_address"
    id = Column(Integer,primary_key=True,autoincrement=True)
    street = Column(String(50),nullable=False)
    name = Column(String(200),nullable=False)
    ext_number = Column(String(10),nullable=False)
    zip_code = Column(Integer,nullable=False)
    suburb = Column(String(100),nullable=False)
    city = Column(String(100),nullable=False)
    phone = Column(String(12),nullable=False)
    client_id = Column(Integer,ForeignKey('esc_client.id'),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getStreet(self):
        return self.street
    
    def setStreet(self,street):
        self.street=street
    
    def getName(self):
        return self.name
    
    def setName(self,name):
        self.name=name
    
    def getExtNumber(self):
        return self.ext_number
    
    def setExtNumber(self,extNumber):
        self.ext_number = extNumber

    def getZipCode(self):
        return self.zip_code

    def setZipCode(self,zipCode):
        self.zip_code=zipCode

    def getSuburb(self):
        return self.suburb

    def setSuburb(self,suburb):
        self.suburb=suburb

    def getCity(self):
        return self.city

    def setCity(self,city):
        self.city=city
    
    def getPhone(self):
        return self.phone

    def setPhone(self,phone):
        self.phone=phone
    
    def getClientId(self):
        return self.client_id

    def setClientId(self,clientId):
        self.client_id=clientId
    

class PaymentMethod(Base):
    __tablename__ = "esc_payment_method"
    id = Column(Integer,primary_key=True,autoincrement=True)
    cardholder = Column(String(200),nullable=False)
    token = Column(String(200),nullable=False)
    month_expiration = Column(Integer,nullable=False)
    year_expiration = Column(Integer,nullable=False)
    client_id = Column(Integer,ForeignKey('esc_client.id'),nullable=False)

    def getId(self):
        return self.id
    
    def setId(self,id):
        self.id = id

    def getCardholder(self):
        return self.cardholder
    
    def setCardholder(self,cardholder):
        self.cardholder=cardholder
    
    def getToken(self):
        return self.token
    
    def setToken(self,token):
        self.token=token
    
    def getMonthExpiration(self):
        return self.month_expiration
    
    def setMonthExpiration(self,monthExpiration):
        self.month_expiration = monthExpiration
    
    def getYearExpiration(self):
        return self.year_expiration
    
    def setYearExpiration(self,yearExpiration):
        self.year_expiration = yearExpiration

    def getClientId(self):
        return self.client_id

    def setClientId(self,clientId):
        self.client_id=client_id

class Order(Base):
    __tablename__ = "esc_order"
    id = Column(Integer,primary_key=True,autoincrement=True)
    cart_id = Column(Integer,ForeignKey('esc_cart.id'),nullable=False)
    status_id = Column(Integer,ForeignKey('esc_status_order.id'),nullable=False)
    address_id = Column(Integer,ForeignKey('esc_address.id'),nullable=False)
    payment_id = Column(Integer,ForeignKey('esc_client.id'),nullable=False)
    delivery_id = Column(Integer,ForeignKey('esc_client.id'),nullable=False)
    created_at = Column(DateTime,nullable=False)




class PersonModel(AbstractModel):

    def __init__(self, url):
        super(PersonModel,self).__init__(url)
        self.url=url

    def createPerson(self,name,lastName):
        person = Person()
        person.setName(name)
        person.setLastName(lastName)
        self.insert(person)

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
