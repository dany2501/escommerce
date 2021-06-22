from dto.Client import Client
from dto.Product import Product
from dto.Cart import Cart
from dto.Address import Address
from dto.Payment import Payment
from dto.Order import Order

class Mapper():

    def mapToClient(self,name,email,token):
        return Client(name,email,token)

    def mapToProduct(self,product,image):
        if product is not None:
            return Product(product.getId(),product.getName(),product.getDescription(),str(product.getPrice()),product.getSku(),product.getStock(),product.getCategoryId(),image)

    def mapToCart(self,product,qty,image):
        return Cart(self.mapToProduct(product,image),qty)

    def mapToAddress(self,address):
        name = address.getName().split(" ")
        return Address(name.pop(0),name,address.getStreet(),address.getExtNumber(),address.getCity(),address.getSuburb(),address.getZipCode(),address.getPhone(),address.getId())
    
    def mapToPayment(self,payment,card,digits):
        return Payment(payment.getId(),payment.getCardholder(),card,digits,payment.getYearExpiration(),payment.getMonthExpiration(),payment.getCvv())

