from model.ClientModel import ClientModel
from rest.controller.Controller import Controller
from model.UserModel import UserModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from cerberus.responses.BodyRS import BodyRS
from cerberus.dtos.Error import Error


class EmailController(Controller):
    def __init__(self):
        super(EmailController, self).__init__()


    def validateEmail(self,token=None,code=None,email=None):
        if code is not None:
            bodyRS = BodyRS(True)
            headerRS = HeaderRS()
            url = self.getUrl()
            if token != "null":
                client = ClientModel(url).getDataClient(token)
            elif email != "null" and email != "":
                client = ClientModel(url).getClientByEmailCode(email)
            if client is not None:
                if int(client[1].getCode()) == int(code):
                    if client[1].getStatusId()==2:
                        user = UserModel(url).updateUserStatus(client[1].getId(),1)
                        if user is not None:
                            return Response(headerRS,bodyRS)
                        else:
                            bodyRS = BodyRS(False,Error(1001,"Ocurrió un error al válidar el correo."))
                            return Response(headerRS,bodyRS)
                    else:
                        bodyRS = BodyRS(False,Error(1004,"Correo válidado anteriormente."))
                        return Response(headerRS,bodyRS)

                else:
                    bodyRS = BodyRS(False,Error(1002,"Código inválido"))
                    return Response(headerRS,bodyRS)
            else:
                bodyRS = BodyRS(False,Error(1003,"No se encontró el usuario"))
                return Response(headerRS,bodyRS)
                    
