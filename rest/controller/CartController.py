from dto.Cart import Cart
from model.ProductModel import ProductModel
from model.CartModel import CartModel
from rest.controller.Controller import Controller
from datetime import datetime
from model.ClientModel import ClientModel
from model.ProductModel import ProductModel
from model.CartModel import CartModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.CartRS import CartRS
from mappers.mapper import Mapper
from cerberus.dtos.Error import Error


class CartController(Controller):
    def __init__(self):
        super(CartController, self).__init__()

    def addProduct(self, token, productId, qty,cartType):
        if token is not None and productId is not None:
            bodyRS = CartRS(True)
            headerRS = HeaderRS()
            url = self.getUrl()
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId(),cartType)
                if cart is None:
                    cart = CartModel(url).createCart(client[0].getId(), 1, datetime.now(),cartType)
                product = ProductModel(url).getProductById(productId)
                if product is not None:
                    if product.getStock() >= int(qty):
                        if int(cartType) ==3:
                            CartModel(url).deleteProducts(cart.getId())
                        CartModel(url).addProductToCart(cart.getId(), product.getId(), qty)
                        products = CartModel(url).getProductsCart(cart.getId())
                        if products is not None:
                            cartResponse = []
                            for p in products:
                                image = ProductModel(url).getImageByProductId(p.getProductId())
                                cartResponse.append(Mapper().mapToCart(ProductModel(url).getProductById(p.getProductId()),p.getQty(),image.getUrl()))
                            bodyRS.setProducts(cartResponse)
                            return Response(headerRS, bodyRS)
                        else:
                            bodyRS = CartRS(False, Error(8004, "Stock insuficiente"))
                            headerRS = HeaderRS()
                            return Response(headerRS, bodyRS)
                    else:
                        bodyRS = CartRS(False, Error(8003, "Stock insuficiente"))
                        headerRS = HeaderRS()
                        return Response(headerRS, bodyRS)
            else:
                bodyRS = CartRS(False, Error(8002, "Usuario no encontrado"))
                headerRS = HeaderRS()
                return Response(headerRS, bodyRS)
        else:
            bodyRS = CartRS(False, Error(8001, "Datos inválidos"))
            headerRS = HeaderRS()
            return Response(headerRS, bodyRS)

    def getProducts(self, token,cartType):
        if token is not None:
            bodyRS = CartRS(True)
            headerRS = HeaderRS()
            url = self.getUrl()
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId(),cartType)
                if cart is not None:
                    products = CartModel(url).getProductsCart(cart.getId())
                    if products is not None:
                        cartResponse = []
                        for p in products:
                            image = ProductModel(url).getImageByProductId(p.getProductId())
                            cartResponse.append(
                                Mapper().mapToCart(
                                    ProductModel(url).getProductById(p.getProductId()),
                                    p.getQty(),
                                    image.getUrl(),
                                )
                            )
                        bodyRS.setProducts(cartResponse)
                        return Response(headerRS, bodyRS)
                else:
                    bodyRS = CartRS(False, Error(7001, "Producto no encontrado"))
                    headerRS = HeaderRS()
                    return Response(headerRS, bodyRS)
            else:
                bodyRS = CartRS(False, Error(7002, "Usuario no encontrado"))
                headerRS = HeaderRS()
                return Response(headerRS, bodyRS)
        else:
            bodyRS = CartRS(False, Error(7001, "No hay sesión"))
            headerRS = HeaderRS()
            return Response(headerRS, bodyRS)

    def deleteProducts(self, token,cartType):
        headerRS = HeaderRS()
        if token is not None:
            bodyRS = CartRS(True)
            url = self.getUrl()
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                cart = CartModel(url).getCartByClientId(client[0].getId(),cartType)
                if cart is not None:
                    delete = CartModel(url).deleteProducts(cart.getId())
                    if delete:
                        return Response(headerRS, bodyRS)
                else:
                    bodyRS = CartRS(False, Error(6002, "No cuentas con productos"))
                    return Response(headerRS, bodyRS)
            else:
                bodyRS = CartRS(False, Error(6001, "Cliente no encontrado"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = CartRS(False, Error(6003, "No se encontró al cliente"))
            return Response(headerRS, bodyRS)

    def deleteProduct(self,token,productId,cartType):
        headerRS = HeaderRS()
        if token is not None:
            if productId is not None:
                bodyRS = CartRS(True)
                url = self.getUrl()
                client = ClientModel(url).getDataClient(token)
                if client is not None:
                    cart = CartModel(url).getCartByClientId(client[0].getId(),cartType)
                    if cart is not None:
                        success = CartModel(url).deleteProductById(cart.getId(),productId)
                        if success:
                            return Response(headerRS,bodyRS)
                        else:
                            bodyRS = CartRS(False,Error(9000,"No se pudo eliminar el producto"))
                            return Response(headerRS,bodyRS)
                    else:
                        bodyRS = CartRS(False,Error(9000,"No se pudo eliminar el producto"))
                        return Response(headerRS,bodyRS)
                else:
                    bodyRS = CartRS(False,Error(9001,"Cliente no encontrado"))
                    return Response(headerRS,bodyRS)
            else:
                bodyRS = CartRS(False,Error(9002,"Producto no encontrado"))
                return Response(headerRS,bodyRS)
        else:
            bodyRS = CartRS(False,Error(9003,"Token inválido"))
            return Response(headerRS,bodyRS)



