import os
from flask import Flask
from flask_restx import Api, Resource, Namespace

app = Flask(__name__)
api = Api(app)
    
# Get Environment
MAC_ADDR = os.environ['MAC_ADDR']
BROADCAST_IP_ADDR = os.environ['BROADCAST_IP_ADDR']


@api.route('/wol')
class wol(Resource):
    def get(self):
        ret = os.popen(f'python ./wol.py {MAC_ADDR} {BROADCAST_IP_ADDR}').read().rstrip()
        if 'OK' == ret:
            return {'result' : 'OK'}
        else:
            return {'result' : ret}

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
