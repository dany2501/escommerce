from model.ZipCodeModel import ZipCodeModel
from rest.controller.Controller import Controller
from model.ClientModel import ClientModel
from model.AddressModel import AddressModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.AddressRS import AddressRS
from mappers.mapper import Mapper
from cerberus.dtos.Error import Error


class AddressController(Controller):
    def __init__(self):
        super(AddressController, self).__init__()

    def createAddress(self, address, token):
        bodyRS = AddressRS(True)
        headerRS = HeaderRS()

        if address is not None:
            url = self.getUrl()
            if token is not None:
                client = ClientModel(url).getDataClient(token)
                if client is not None:
                    zip = ZipCodeModel(url).findZipCode(int(address["zipCode"]))
                    if zip is not None:
                        AddressModel(url).createAddress(
                            address["name"],
                            address["street"],
                            address["extNum"],
                            address["zipCode"],
                            address["suburb"],
                            address["city"],
                            address["phone"],
                            client[0].getId(),
                        )
                        address = AddressModel(url).getAddressByClientId(client[0].getId())
                        if address is not None:
                            return Response(headerRS, bodyRS)
                    else:
                        bodyRS = AddressRS(False, Error(1002, "Código postal inválido"))
                        return Response(headerRS, bodyRS)

                else:
                    bodyRS = AddressRS(False, Error(1001, "No se encontró al usuario"))
                    return Response(headerRS, bodyRS)
            else:
                bodyRS = AddressRS(False, Error(1001, "No se encontró al usuario"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = AddressRS(
                False, Error(1000, "No se encontraron datos para guardar")
            )
            return Response(headerRS, bodyRS)

    def getAddress(self, token):
        bodyRS = AddressRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        client = ClientModel(url).getDataClient(token)
        if client is not None:
            address = AddressModel(url).getAddressByClientId(client[0].getId())
            if address is not None:
                listAddress =[]
                for a in address:
                    listAddress.append(Mapper().mapToAddress(a))
                bodyRS.setAddress(listAddress)
                return Response(headerRS, bodyRS)
            else:
                bodyRS = AddressRS(False, Error(1001, "No se la dirección de envío"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = AddressRS(False, Error(8001, "No se encontró al usuario"))
            return Response(headerRS, bodyRS)
