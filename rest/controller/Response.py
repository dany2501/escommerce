from flask import Response
import json

class ResponseFactory():

    def toResponse(data,origin=None,method=None):
        response = Response(json.dumps(data.getBodyRS()),mimetype="application/json")
        response.headers['x-token'] = data.getHeaderRS().getToken()
        response.headers['x-created-at'] = data.getHeaderRS().getCreatedAt()
        response.headers['x-updated-at'] = data.getHeaderRS().getUpdatedAt()
        response.headers['Access-Controll-Allow-Headers'] = 'application/json'
        response.headers['Content-Type'] = 'application/json'

        if not origin is None:
            response.headers['Access-Control-Allow-Credentials'] = 'true'
            response.headers['Access-Control-Allow-Origin'] = origin
            response.headers['Access-Control-Allow-Methods'] = method
            response.headers['Vary'] = "Origin"
        
        return response