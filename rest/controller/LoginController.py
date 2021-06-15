from rest.controller.Controller import Controller
from datetime import date, datetime
from model.ClientModel import ClientModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.responses.Response import Response
from rest.Responses.LoginRS import LoginRS
from mappers.mapper import Mapper
from cerberus.dtos.Error import Error
from uuid import uuid4


class LoginController(Controller):
    def __init__(self):
        super(LoginController, self).__init__()

    def loginUser(self, email, password):
        headerRS = HeaderRS()
        url = self.getUrl()
        if email and password:
            bodyRS = LoginRS(True)
            user = ClientModel(url).getClientByEmail(email)
            if user is not None:
                if user.getStatusId() == 1:
                    client = ClientModel(url).loginClient(email, password)
                    if client is not None:
                        token = str(uuid4())
                        session = ClientModel(url).updateClient(
                            client[0].id, token, datetime.now()
                        )
                        if session:
                            c = Mapper().mapToClient(
                                client[2].getName() + " " + client[2].getLastName() +" "+client[2].getSecondLastName(),
                                client[1].getEmail(),
                                token,
                            )
                            bodyRS.setClient(c)
                            return Response(headerRS, bodyRS)
                    else:
                        bodyRS = LoginRS(False, Error(5002, "Las credenciales no coinciden"))
                        return Response(headerRS, bodyRS)
                else:
                    if user.getStatusId() == 2:
                        bodyRS = LoginRS(False, Error(5003, "Correo no confirmado"))
                    elif user.getStatusId() == 3:
                        bodyRS = LoginRS(False, Error(5004, "Usuario Inactivo"))
                    elif user.getStatusId() == 4:
                        bodyRS = LoginRS(False, Error(5005, "Usuario Bloqueado"))

                    return Response(headerRS, bodyRS)
            else:
                bodyRS = LoginRS(False, Error(5001, "Usuario no encontrado"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = LoginRS(False, Error(5000, "Datos no obtenidos"))
            return Response(headerRS, bodyRS)

    def getDataClient(self, token):
        bodyRS = LoginRS(True)
        headerRS = HeaderRS()
        url = self.getUrl()
        if token:
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                c = Mapper().mapToClient(
                    client[2].getName() + " " + client[2].getLastName(),
                    client[1].getEmail(),
                    client[0].getToken(),
                )
                bodyRS.setClient(c)
                return Response(headerRS, bodyRS)
            else:
                bodyRS = LoginRS(False, Error(3001, "Usuario no encontrado"))
                return Response(headerRS, bodyRS)
        else:
            bodyRS = LoginRS(False, Error(3000, "Token inválido"))

    def logOutUser(self, token):
        url = self.getUrl()
        if token:
            client = ClientModel(url).getDataClient(token)
            if client is not None:
                return True
            else:
                return False
