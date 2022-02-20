#import device_module
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

device_put_args = reqparse.RequestParser()
device_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
device_put_args.add_argument("views", type=int, help="Views of the video is required", required=True)
device_put_args.add_argument("likes", type=int, help="Likes on the video is required", required=True)

devices = {}


def device_id_dne(device_id):
    """Abort if the device_id does not exist (DNE)"""
    if device_id not in devices:
        abort(404, message="device_id does not exist")

def device_id_already_exits(device_id):
    """Abort if the device_id already exists"""
    if device_id in devices:
        abort(409, message="device_id already exists")


class Device(Resource):
    def get(self, device_id):
        """Retrieve information about a device with a given device_id"""
        # Abort if device_id does not exist
        device_id_dne(device_id)
        return devices[device_id]

    def put(self, device_id):
        """"Create a new device with input device_id and insert the information into database"""
        # Abort if the device id already exists
        device_id_already_exits(device_id)
        args = device_put_args.parse_args()
        devices[device_id] = args
        return devices[device_id], 201

    def delete(self, device_id):
        """Delete a device with input device_id"""
        # Abort if the device_id does not exist
        device_id_dne(device_id)
        del devices[device_id]
        return '', 204


api.add_resource(Device, "/device/<int:device_id>")


if __name__ == "__main__":
    app.run(debug=True)
