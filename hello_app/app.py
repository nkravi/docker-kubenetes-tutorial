import socket
import os
import requests
from flask import Flask
from flask_restful import Resource, Api
from flask_restful import reqparse
import json

app = Flask(__name__)
api = Api(app)


class HelloWorld(Resource):
    def get(self, name):
        reqparser = reqparse.RequestParser()
        reqparser.add_argument('ln', required=False)
        args = reqparser.parse_args()
        if args['ln']:
            url = os.environ.get('HOLA_SRV', 'http://localhost:5001/')
            url = url+name
            r = requests.get(url)
            if r.status_code != 200:
                return {"error": str(r)}
            print(r)
            return json.loads(r.text)
        return {'hello': name,
                'myip': socket.gethostbyname(socket.gethostname())}


class Ops(Resource):
    def get(self):
        return 200


api.add_resource(HelloWorld, '/<name>')
api.add_resource(Ops, '/ops/healthz')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5000)
