from rest.controller.Controller import Controller
from datetime import date, datetime
from model.ClientModel import ClientModel
from model.PersonModel import PersonModel
from model.UserModel import User,UserModel
from cerberus.responses.HeaderRS import HeaderRS
from cerberus.dtos.Error import Error
from cerberus.responses.Response import Response
from rest.Responses.SignUpRS import SignUpRS
from uuid import uuid4
from rest.controller.EmailService import EmailService
from random import randint
from rest.controller.EmailService import EmailService
class SignUpController(Controller):
    def __init__(self):
        super(SignUpController,self).__init__()

    
    def registerUser(self,email,password,confirmPass,name,app,apm=None):
        url = self.getUrl()
        if password == confirmPass:
            if email and password:
                bodyRS = SignUpRS(True)
                headerRS = HeaderRS()
                host = str(email.split('@')[1])
                alumno = "alumno.ipn.mx"
                guinda = "gmail.com"
                if host == alumno or host == guinda:
                    u = UserModel(url).getUserByEmail(email)
                    if u is None:
                        person = PersonModel(url).createPerson(name,app,apm)
                        code = self.generateRandomCode(6)
                        if code is not None:
                            user = UserModel(url).createUser(email,password,person.getId(),code)
                            rand_token = str(uuid4())
                            client = ClientModel(url).createClient(datetime.now(),rand_token,datetime.now(),user.getId())
                            if client is not None:
                                EmailService().sendEmailClient(user.getEmail(),code,name)
                                bodyRS.setToken(rand_token)
                                response = Response(headerRS,bodyRS)
                                return response
                    else:
                        bodyRS = SignUpRS(False,Error(4003,"El correo ya está en uso"))
                        headerRS = HeaderRS()
                        return Response(headerRS,bodyRS)
                else:
                    bodyRS = SignUpRS(False,Error(4002,"Correo inválido"))
                    headerRS = HeaderRS()
                    return Response(headerRS,bodyRS)
            else:
                bodyRS = SignUpRS(False,Error(4001,"No hay datos"))
                headerRS = HeaderRS()
                return Response(headerRS,bodyRS)
        else:
            bodyRS = SignUpRS(False,Error(4000,"Las contraseñas no coinciden"))
            headerRS = HeaderRS()
            return Response(headerRS,bodyRS)


    

    def generateRandomCode(self,length):
        range_start = 10**(length-1)
        range_end = (10**length)-1
        return randint(range_start, range_end)
        