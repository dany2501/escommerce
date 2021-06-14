from sqlalchemy import or_
from entities.AbstractModel import AbstractModel
from entities.Person import Product,ProductImage

class ProductModel(AbstractModel):

    def __init__(self, url):
        super(ProductModel,self).__init__(url)
        self.url=url

    def getProducts(self):
        products = self.session.query(Product).all()
        self.session.close()
        if products is not None:
            return products
        else:
            print("Throw Exception")

    def getProductsByCategoryId(self,categoryId):
        products = self.session.query(Product).filter(Product.category_id==categoryId).all()
        self.session.close()
        if products is not None:
            return products
        else:
            print("Throw Exception")

    def getProductById(self,productId):
        product = self.session.query(Product).filter(Product.id==productId).first()
        self.session.close()
        if product is not None:
            return product
        else:
            print("Throw Exception")

    def getImageByProductId(self,productId):
        image = self.session.query(ProductImage).filter(ProductImage.product_id==productId).first()
        self.session.close()
        if image is not None:
            return image
        else:
            return None

    def getProductsByName(self,name):
        products = self.session.query(Product).filter(or_(Product.description.like("%"+name+"%"),Product.name.like("%"+name+"%"))).all()
        self.session.close()
        if products is not None:
            return products
        else:
            return None