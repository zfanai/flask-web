#encoding:utf8

from flask import Flask
from flask import Response
from flask import request
from werkzeug.datastructures import Headers

class MyResponse(Response):
    def __init__(self, response=None, **kwargs):
        #print 'dfef'
        kwargs['headers'] = ''
        headers = kwargs.get('headers')
        # 跨域控制 
        origin = ('Access-Control-Allow-Origin', '*')
        methods = ('Access-Control-Allow-Methods', 'HEAD, OPTIONS, GET, POST, DELETE, PUT')
        allow=('Access-Control-Allow-Headers', 'x-request-with,content-type')
        if headers:
            headers.add(*origin)
            headers.add(*methods)
            headers.add(*allow)
        else:
            headers = Headers([origin, methods, allow])
        #print 'headers:', headers, request.method, request.path
        kwargs['headers'] = headers
        return super(MyResponse, self).__init__(response, **kwargs)
    
def create_app():
    app=Flask(__name__)
    app.response_class=MyResponse
    
    from .views.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    return app
