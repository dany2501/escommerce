from rest.controller.Controller import Controller
from model.ProductModel import ProductModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.ProductsRS import ProductsRS
from mappers.mapper import Mapper
from cerberus.dtos.Error import Error
import random


class ProductController(Controller):
    def __init__(self):
        super(ProductController, self).__init__()

    def getProducts(self):
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        products = ProductModel(url).getProducts()
        if products is not None:
            productList = []
            lr = random.sample(products, len(products))
            for product in lr:
                image = ProductModel(url).getImageByProductId(product.getId())
                if image is not None:
                    productList.append(Mapper().mapToProduct(product, image.getUrl()))
            bodyRS.setProducts(productList)
            return Response(headerRS, bodyRS)
        else:
            bodyRS = ProductsRS(False, Error(2000, "No hay productos registrados"))
            return Response(headerRS, bodyRS)
    
    def getProductsByCategoryId(self,categoryId=None):
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        if int(categoryId) == 0:
            products = ProductModel(url).getProducts()
        else:
            products = ProductModel(url).getProductsByCategoryId(categoryId)
        if products is not None:
            productList = []
            lr = random.sample(products, len(products))
            for product in lr:
                image = ProductModel(url).getImageByProductId(product.getId())
                productList.append(Mapper().mapToProduct(product, image.getUrl()))
            bodyRS.setProducts(productList)
            return Response(headerRS, bodyRS)
        else:
            bodyRS = ProductsRS(False, Error(2000, "No hay productos registrados"))
            return Response(headerRS, bodyRS)

    def getProduct(self, productId):
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()

        url = self.getUrl()

        if productId is not None:
            product = ProductModel(url).getProductById(productId)
            image = ProductModel(url).getImageByProductId(product.getId())
            if product is not None:
                bodyRS.setProducts(Mapper().mapToProduct(product, image.getUrl()))
                return Response(headerRS, bodyRS)
            else:
                bodyRS = ProductsRS(False, Error(2001, "No se encontró el producto"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = ProductsRS(False, Error(2001, "No se encontró el producto"))
            return Response(headerRS, bodyRS)

    def getProductByName(self,name):
        bodyRS = ProductsRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        if name is not None:
            products = ProductModel(url).getProductsByName(name)
            if products is not None:
                productList = []
                for product in products:
                    image = ProductModel(url).getImageByProductId(product.getId())
                    if image is not None:
                        productList.append(Mapper().mapToProduct(product, image.getUrl()))
                bodyRS.setProducts(productList)
                return Response(headerRS, bodyRS)
            else:
                bodyRS = ProductsRS(False, Error(2001, "No se encontraron productos"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = ProductsRS(False, Error(2002, "Ocurrió un error al buscar productos"))
            return Response(headerRS, bodyRS)


