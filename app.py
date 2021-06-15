from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_mail import Mail
#config enviroment
from dynaconf import FlaskDynaconf
config_cache = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'cache',
    'CACHE_DEFAULT_TIMEOUT': 3600,
}

#ENV_FOR_DYNACONF production, development or default, staging
ENV_FOR_DYNACONF = "default"
GLOBAL_ENV_FOR_DYNACONF = "skeleton-flask-v1"
ENVVAR_FOR_DYNACONF = "env_config.toml"
MERGE_ENABLED_FOR_DYNACONF= "true"
SETTINGS_MODULE_FOR_DYNACONF= "env_config.toml"

app = Flask(__name__)
api = Api(app)
app.config.from_mapping(config_cache)

#set config enviroment app
FlaskDynaconf(
    app,
    GLOBAL_ENV_FOR_DYNACONF=GLOBAL_ENV_FOR_DYNACONF,
    ENVVAR_FOR_DYNACONF=ENVVAR_FOR_DYNACONF,
    MERGE_ENABLED_FOR_DYNACONF= MERGE_ENABLED_FOR_DYNACONF,
    SETTINGS_MODULE_FOR_DYNACONF= SETTINGS_MODULE_FOR_DYNACONF,
    ENV_FOR_DYNACONF= ENV_FOR_DYNACONF
)
mail_settings = {
    "MAIL_SERVER": app.config.MAIL_SERVER,
    "MAIL_PORT": app.config.MAIL_PORT,
    "MAIL_USE_TLS": app.config.MAIL_USE_TLS,
    "MAIL_USE_SSL": app.config.MAIL_USE_SSL,
    "MAIL_USERNAME": app.config.MAIL_USERNAME,
    "MAIL_PASSWORD": app.config.MAIL_PASSWORD,
}

app.config.update(mail_settings)

app.config['SQLALCHEMY_BINDS'] = {
    "Database_Name":"mysql+pymysql://root:hecd010225@127.0.0.1/escommerce"
}

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
#Set Up Mongoengine
db = SQLAlchemy(app)
mail = Mail(app)


from flask import request
from rest.controller.LoginController import LoginController
from rest.resource.Login import LoginResource
from rest.resource.SignUp import SignUpResource
from rest.resource.Products import ProductsResource
from rest.resource.Cart import CartResource
from rest.resource.Address import AddressResource
from rest.resource.Email import EmailResource
from rest.resource.Order import OrderResource
from rest.resource.Payment import PaymentResource

api.add_resource(SignUpResource,'/sign-up')
api.add_resource(LoginResource,'/login')
api.add_resource(ProductsResource,'/products')
api.add_resource(CartResource,'/cart')
api.add_resource(AddressResource,'/address')
api.add_resource(EmailResource,'/email')
api.add_resource(OrderResource,'/order')
api.add_resource(PaymentResource,'/payment')

@app.route('/logout')
def logout():
    token = request.headers['token']
    if token:
        return jsonify(LoginController().logOutUser(token))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8000')