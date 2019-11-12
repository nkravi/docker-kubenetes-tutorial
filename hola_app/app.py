import socket
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class HollaWorld(Resource):
    def get(self, name):
        return {'hola': name,
         'myip': socket.gethostbyname(socket.gethostname())}


class Ops(Resource):
    def get(self):
        return 200


api.add_resource(HollaWorld, '/<name>')
api.add_resource(Ops, '/ops/healthz')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=5001)
