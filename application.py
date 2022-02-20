#import device_module
from flask import Flask
from flask_restful import Api, Resource, reqparse, abort

application = Flask(__name__)
api = Api(application)

device_put_args = reqparse.RequestParser()
device_put_args.add_argument("device_id", type=int, help="Must have a device_id", required=True)
device_put_args.add_argument("patient_assigned", type=int, help="Must have a patient_id assigned", required=True)
device_put_args.add_argument("type", type=str, help="Must have a device_type", required=True)
device_put_args.add_argument("measurement", help="Must have a measurement", required=True)
device_put_args.add_argument("MAC", type=str, help="Must have a MAC address", required=True)
device_put_args.add_argument("purchase_date", type=str, help="Must have a device_type", required=True)
device_put_args.add_argument("model_number", type=int, help="Must have a model_number", required=True)
device_put_args.add_argument("model_name", type=str, help="Must have a model_name", required=True)
device_put_args.add_argument("serial_number", type=int, help="Must have a serial_number", required=True)


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


api.add_resource(Device, "/device/<string:device_id>")


if __name__ == "__main__":
    application.run(debug=True)
