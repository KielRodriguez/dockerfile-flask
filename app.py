from flask import Flask, request
from flask_restful import Api, Resource

from config import configure_app

import json

from api.v1.resources.hello_world import HelloWorld

app = Flask(__name__)

configure_app(app)
api = Api(app, prefix='/api/v1')

api.add_resource(HelloWorld, '/hello-world')

if __name__ == '__main__':
    app.run()
