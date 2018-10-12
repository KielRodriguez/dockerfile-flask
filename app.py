from flask import Flask, request
from flask_restful import Api, Resource
from flask_mysqldb import MySQL

from config import configure_app

import json

from api.v1.resources.hello_world import HelloWorld
from api.v1.resources.test_connection import TestConnection

app = Flask(__name__)

configure_app(app)
api = Api(app, prefix='/api/v1')

mysql = MySQL(app)
api.add_resource(HelloWorld, '/hello-world')
api.add_resource(TestConnection, '/date')

if __name__ == '__main__':
    app.run()
